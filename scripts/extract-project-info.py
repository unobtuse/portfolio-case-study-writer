#!/usr/bin/env python3
"""
Extract structured project information from PRD or project summary files.

Parses uploaded markdown, PDF, or text files to identify:
- Project name and description
- Technical requirements and stack
- Timeline and milestones
- Key features and functionality
- Stakeholders and success criteria

Usage:
    python3 extract-project-info.py <file-path>
"""

import re
import sys
import json
from pathlib import Path
from typing import Dict, List, Optional


def extract_project_name(content: str) -> Optional[str]:
    """
    Look for project name in various formats.
    Priority: H1 heading > "Project Name:" label > document title
    """
    # Try markdown H1
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()

    # Try explicit "Project Name:" label
    match = re.search(r'Project\s+Name:?\s*(.+?)(?:\n|$)', content, re.IGNORECASE | re.MULTILINE)
    if match:
        return match.group(1).strip()

    # Try "Title:" label
    match = re.search(r'Title:?\s*(.+?)(?:\n|$)', content, re.IGNORECASE | re.MULTILINE)
    if match:
        return match.group(1).strip()

    return None


def extract_description(content: str) -> Optional[str]:
    """Extract project description or summary."""
    # Look for summary/overview/description sections
    patterns = [
        r'(?:Summary|Overview|Description):?\s*\n\s*(.+?)(?:\n\n|\n#)',
        r'(?:Project\s+)?(?:Summary|Overview):?\s*(.+?)(?:\n\n|\n#)',
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        if match:
            desc = match.group(1).strip()
            # Limit to first paragraph if multiple
            first_para = desc.split('\n\n')[0]
            return first_para.strip()

    # Fallback: Look for first paragraph after H1
    match = re.search(r'^#\s+.+?\n\s*(.+?)(?:\n\n|\n#)', content, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1).strip()[:500]  # Limit length

    return None


def extract_tech_stack(content: str) -> List[str]:
    """Find technology mentions and stack information."""
    techs = []

    # Look for explicit tech stack sections
    tech_patterns = [
        r'(?:Technologies?|Tech\s+Stack|Stack):?\s*\n?\s*(.+?)(?:\n\n|\n#)',
        r'(?:Tech|Technologies|Stack):?\s*(?:\n\s*[-*•]\s*|\n)(.+?)(?:\n\n|\n#)',
    ]

    for pattern in tech_patterns:
        match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        if match:
            tech_text = match.group(1).strip()
            # Split by common separators
            items = re.split(r'[,\n•\-\*]', tech_text)
            techs.extend([t.strip() for t in items if t.strip()])

    # Common technology patterns to search for
    tech_keywords = [
        r'\b(React|Vue|Angular|Svelte|Next\.js|Nuxt|Gatsby)\b',
        r'\b(Node\.js|Express|Django|Flask|Rails|Laravel|FastAPI)\b',
        r'\b(PostgreSQL|MySQL|MongoDB|Redis|SQLite|DynamoDB)\b',
        r'\b(TypeScript|JavaScript|Python|Ruby|PHP|Go|Rust|Java)\b',
        r'\b(AWS|Azure|GCP|Heroku|Vercel|Netlify|DigitalOcean)\b',
        r'\b(Docker|Kubernetes|Terraform|Jenkins|GitHub\s+Actions)\b',
        r'\b(Figma|Sketch|Adobe\s+XD|Photoshop|Illustrator)\b',
    ]

    for pattern in tech_keywords:
        matches = re.findall(pattern, content, re.IGNORECASE)
        techs.extend(matches)

    # Remove duplicates and clean
    unique_techs = []
    seen = set()
    for tech in techs:
        tech_lower = tech.lower()
        if tech_lower not in seen and tech:
            seen.add(tech_lower)
            unique_techs.append(tech)

    return unique_techs[:15]  # Limit to top 15


def extract_timeline(content: str) -> Dict[str, Optional[str]]:
    """Extract timeline, dates, or duration information."""
    timeline = {
        'start_date': None,
        'end_date': None,
        'duration': None
    }

    # Look for explicit timeline section
    match = re.search(r'Timeline:?\s*(.+?)(?:\n\n|\n#)', content, re.IGNORECASE | re.MULTILINE)
    if match:
        timeline['duration'] = match.group(1).strip()

    # Look for date ranges (various formats)
    date_patterns = [
        r'(\d{1,2}/\d{1,2}/\d{2,4})\s*[-–—to]+\s*(\d{1,2}/\d{1,2}/\d{2,4})',
        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4}\s*[-–—to]+\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4}',
        r'(\d{4}-\d{2}-\d{2})\s*[-–—to]+\s*(\d{4}-\d{2}-\d{2})',
    ]

    for pattern in date_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            timeline['start_date'] = match.group(1)
            timeline['end_date'] = match.group(2)
            break

    # Look for duration mentions
    duration_pattern = r'(\d+\s*(?:weeks?|months?|days?|years?))'
    match = re.search(duration_pattern, content, re.IGNORECASE)
    if match and not timeline['duration']:
        timeline['duration'] = match.group(1)

    return timeline


def extract_key_features(content: str) -> List[str]:
    """Extract key features or requirements."""
    features = []

    # Look for features/requirements sections
    section_patterns = [
        r'(?:Key\s+)?Features:?\s*\n(.+?)(?:\n\n|\n#)',
        r'Requirements:?\s*\n(.+?)(?:\n\n|\n#)',
        r'Functionality:?\s*\n(.+?)(?:\n\n|\n#)',
    ]

    for pattern in section_patterns:
        match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        if match:
            feature_text = match.group(1)
            # Extract bullet points
            bullets = re.findall(r'[-*•]\s*(.+)', feature_text)
            features.extend([b.strip() for b in bullets if b.strip()])

    # Look for numbered lists
    numbered = re.findall(r'\d+\.\s+(.+)', content)
    if numbered and not features:
        features.extend([n.strip() for n in numbered[:10]])

    return features[:10]  # Limit to top 10


def extract_stakeholders(content: str) -> List[str]:
    """Extract stakeholders or team information."""
    stakeholders = []

    # Look for stakeholders/team sections
    patterns = [
        r'Stakeholders?:?\s*(.+?)(?:\n\n|\n#)',
        r'Team:?\s*(.+?)(?:\n\n|\n#)',
        r'Client:?\s*(.+?)(?:\n\n|\n#)',
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
        if match:
            stakeholder_text = match.group(1).strip()
            items = re.split(r'[,\n•\-\*]', stakeholder_text)
            stakeholders.extend([s.strip() for s in items if s.strip()])

    return stakeholders[:5]


def extract_success_criteria(content: str) -> List[str]:
    """Extract success criteria, goals, or metrics."""
    criteria = []

    # Look for success/goals sections
    patterns = [
        r'Success\s+Criteria:?\s*\n(.+?)(?:\n\n|\n#)',
        r'Goals?:?\s*\n(.+?)(?:\n\n|\n#)',
        r'Objectives?:?\s*\n(.+?)(?:\n\n|\n#)',
        r'Metrics?:?\s*\n(.+?)(?:\n\n|\n#)',
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        if match:
            criteria_text = match.group(1)
            bullets = re.findall(r'[-*•]\s*(.+)', criteria_text)
            criteria.extend([c.strip() for c in bullets if c.strip()])

    return criteria[:8]


def extract_project_info(file_path: str) -> Dict:
    """
    Main extraction function.
    Returns structured JSON with all extracted data.
    """
    path = Path(file_path)

    if not path.exists():
        return {'error': f'File not found: {file_path}'}

    # Read file content
    try:
        content = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        try:
            content = path.read_text(encoding='latin-1')
        except Exception as e:
            return {'error': f'Could not read file: {e}'}

    # Extract all information
    extracted = {
        'file_path': file_path,
        'project_name': extract_project_name(content),
        'description': extract_description(content),
        'tech_stack': extract_tech_stack(content),
        'timeline': extract_timeline(content),
        'key_features': extract_key_features(content),
        'stakeholders': extract_stakeholders(content),
        'success_criteria': extract_success_criteria(content),
        'extraction_confidence': 'high' if extract_project_name(content) else 'low'
    }

    return extracted


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python3 extract-project-info.py <file-path>")
        sys.exit(1)

    file_path = sys.argv[1]
    result = extract_project_info(file_path)

    # Pretty print JSON
    print(json.dumps(result, indent=2))

    # Return appropriate exit code
    if 'error' in result:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
