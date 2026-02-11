#!/usr/bin/env python3
"""
Validate case study quality and completeness.

Checks:
- Word count in target range
- Required sections present
- Metrics included (at least 2)
- Technical specificity
- AI-tell vocabulary detection
- Markdown formatting

Usage:
    python3 validate-case-study.py <file-path> <format-type>

Arguments:
    file-path: Path to case study markdown file
    format-type: Either 'detailed' or 'concise'
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


# AI-tell vocabulary that sounds generic/automated
AI_TELLS = [
    'delve', 'leverage', 'robust', 'seamless', 'cutting-edge',
    'groundbreaking', 'utilize', 'facilitate', 'tapestry',
    'landscape', 'paradigm', 'synergy', 'holistic', 'innovative',
    'revolutionary', 'game-changing', 'disruptive', 'state-of-the-art',
    'best-in-class', 'world-class', 'next-generation',
]

# Vague technical phrases to avoid
VAGUE_PHRASES = [
    'modern framework', 'latest technology', 'best practices',
    'industry standard', 'cutting edge', 'advanced techniques',
    'sophisticated approach', 'powerful tools', 'robust solution',
    'scalable architecture', 'efficient system', 'optimized code',
]

# Required sections for detailed case studies
REQUIRED_SECTIONS_DETAILED = [
    'overview', 'context', 'background', 'process', 'development',
    'challenge', 'result', 'impact', 'reflection', 'takeaway'
]

# Required sections for concise case studies
REQUIRED_SECTIONS_CONCISE = [
    'challenge', 'approach', 'result'
]


def count_words(content: str) -> int:
    """Count words in content (excluding code blocks and YAML frontmatter)."""
    # Remove YAML frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    # Remove code blocks
    content = re.sub(r'```[\s\S]*?```', '', content)

    # Remove inline code
    content = re.sub(r'`[^`]+`', '', content)

    # Remove markdown formatting
    content = re.sub(r'[#*_\[\]\(\)]+', '', content)

    # Count words
    words = content.split()
    return len(words)


def check_word_count(word_count: int, format_type: str) -> Tuple[bool, str]:
    """Check if word count is within target range."""
    if format_type == 'detailed':
        if word_count < 1500:
            return False, f"Word count too low: {word_count} (target: 1500-2500)"
        elif word_count > 2500:
            return False, f"Word count too high: {word_count} (target: 1500-2500)"
        else:
            return True, f"Word count good: {word_count} (target: 1500-2500)"
    else:  # concise
        if word_count < 500:
            return False, f"Word count too low: {word_count} (target: 500-800)"
        elif word_count > 800:
            return False, f"Word count too high: {word_count} (target: 500-800)"
        else:
            return True, f"Word count good: {word_count} (target: 500-800)"


def check_required_sections(content: str, format_type: str) -> Tuple[List[str], List[str]]:
    """
    Check for required sections.
    Returns (found_sections, missing_sections)
    """
    required = REQUIRED_SECTIONS_DETAILED if format_type == 'detailed' else REQUIRED_SECTIONS_CONCISE

    # Convert content to lowercase for matching
    content_lower = content.lower()

    found = []
    missing = []

    for section in required:
        # Check if section keyword appears in a heading
        if re.search(rf'##?\s+.*{section}', content_lower):
            found.append(section)
        else:
            missing.append(section)

    return found, missing


def check_metrics(content: str) -> Tuple[int, List[str]]:
    """
    Check for quantifiable metrics.
    Returns (count, examples)
    """
    examples = []

    # Percentage pattern
    percentages = re.findall(r'\d+%', content)
    examples.extend(percentages[:3])

    # Multiplier pattern (2x, 3.5x, etc.)
    multipliers = re.findall(r'\d+(?:\.\d+)?x\b', content, re.IGNORECASE)
    examples.extend(multipliers[:3])

    # Dollar amounts
    dollars = re.findall(r'\$\d[\d,]*(?:\.\d{2})?(?:K|M|k|m)?\b', content)
    examples.extend(dollars[:3])

    # Time measurements with numbers
    times = re.findall(r'\d+\s*(?:seconds?|minutes?|hours?|days?|weeks?|months?|ms|s)\b', content, re.IGNORECASE)
    examples.extend(times[:3])

    # User/visitor counts
    users = re.findall(r'\d[\d,]*\s*(?:users?|visitors?|customers?|sessions?)\b', content, re.IGNORECASE)
    examples.extend(users[:3])

    # Remove duplicates
    unique_examples = list(dict.fromkeys(examples))

    return len(unique_examples), unique_examples[:5]


def check_ai_tells(content: str) -> List[str]:
    """Check for AI-tell vocabulary."""
    content_lower = content.lower()
    found = []

    for tell in AI_TELLS:
        if tell in content_lower:
            # Count occurrences
            count = content_lower.count(tell)
            found.append(f"{tell} ({count}x)")

    return found


def check_vague_language(content: str) -> List[str]:
    """Check for vague technical phrases."""
    content_lower = content.lower()
    found = []

    for phrase in VAGUE_PHRASES:
        if phrase in content_lower:
            found.append(phrase)

    return found


def check_technical_specificity(content: str) -> Dict:
    """
    Check for technical specificity indicators.
    Good: Specific technology names, version numbers, concrete examples
    Bad: Generic terms, vague descriptions
    """
    indicators = {
        'specific_technologies': [],
        'version_numbers': [],
        'code_snippets': 0,
        'generic_terms': 0
    }

    # Look for specific technology names
    tech_pattern = r'\b(React|Vue|Angular|Node\.js|Django|PostgreSQL|MongoDB|TypeScript|Python|AWS|Docker|Kubernetes|Next\.js|Express|Redis|GraphQL|REST|WebSocket)\b'
    techs = re.findall(tech_pattern, content, re.IGNORECASE)
    indicators['specific_technologies'] = list(set(techs))[:10]

    # Look for version numbers
    versions = re.findall(r'(?:v|version\s+)?\d+\.\d+(?:\.\d+)?', content, re.IGNORECASE)
    indicators['version_numbers'] = versions[:5]

    # Count code snippets
    code_blocks = re.findall(r'```[\s\S]*?```', content)
    indicators['code_snippets'] = len(code_blocks)

    # Count generic terms
    generic_terms = ['framework', 'library', 'tool', 'technology', 'system', 'platform']
    for term in generic_terms:
        # Only count if not preceded by a specific name
        pattern = rf'(?<![\w-]){term}(?![\w-])'
        matches = re.findall(pattern, content, re.IGNORECASE)
        indicators['generic_terms'] += len(matches)

    return indicators


def check_markdown_formatting(content: str) -> List[str]:
    """Check for markdown formatting issues."""
    issues = []

    # Check for placeholder text
    placeholders = re.findall(r'\{\{[^}]+\}\}', content)
    if placeholders:
        issues.append(f"Found {len(placeholders)} unfilled placeholders: {placeholders[:3]}")

    # Check for broken links
    broken_links = re.findall(r'\[.*?\]\(\s*\)', content)
    if broken_links:
        issues.append(f"Found {len(broken_links)} broken/empty links")

    # Check for TODO markers
    todos = re.findall(r'TODO|FIXME|XXX', content, re.IGNORECASE)
    if todos:
        issues.append(f"Found {len(todos)} TODO markers")

    # Check for excessive newlines
    excessive = re.findall(r'\n{4,}', content)
    if excessive:
        issues.append(f"Found {len(excessive)} instances of excessive newlines (4+)")

    return issues


def validate_case_study(file_path: str, format_type: str = 'detailed') -> Dict:
    """
    Main validation function.
    Returns validation results with issues, warnings, and pass/fail status.
    """
    path = Path(file_path)

    if not path.exists():
        return {
            'error': f'File not found: {file_path}',
            'passed': False
        }

    # Read file
    try:
        content = path.read_text(encoding='utf-8')
    except Exception as e:
        return {
            'error': f'Could not read file: {e}',
            'passed': False
        }

    # Initialize results
    results = {
        'file': file_path,
        'format_type': format_type,
        'word_count': 0,
        'issues': [],
        'warnings': [],
        'suggestions': [],
        'passed': True
    }

    # 1. Word count check
    word_count = count_words(content)
    results['word_count'] = word_count
    wc_passed, wc_message = check_word_count(word_count, format_type)
    if not wc_passed:
        results['issues'].append(wc_message)
        results['passed'] = False
    else:
        results['suggestions'].append(wc_message)

    # 2. Required sections check
    found_sections, missing_sections = check_required_sections(content, format_type)
    if missing_sections:
        results['issues'].append(f"Missing required sections: {', '.join(missing_sections)}")
        results['passed'] = False

    # 3. Metrics check
    metric_count, metric_examples = check_metrics(content)
    if metric_count < 2:
        results['warnings'].append(f"Only {metric_count} quantifiable metrics found (target: 2+)")
    else:
        results['suggestions'].append(f"Good: Found {metric_count} metrics - {metric_examples}")

    # 4. AI-tell vocabulary check
    ai_tells = check_ai_tells(content)
    if ai_tells:
        results['warnings'].append(f"AI-tell vocabulary detected: {', '.join(ai_tells)}")

    # 5. Vague language check
    vague = check_vague_language(content)
    if vague:
        results['warnings'].append(f"Vague language detected: {', '.join(vague[:5])}")

    # 6. Technical specificity check
    tech_spec = check_technical_specificity(content)
    if len(tech_spec['specific_technologies']) < 3:
        results['warnings'].append(f"Low technical specificity: only {len(tech_spec['specific_technologies'])} specific technologies named")
    else:
        results['suggestions'].append(f"Good: {len(tech_spec['specific_technologies'])} specific technologies mentioned")

    if tech_spec['code_snippets'] == 0 and format_type == 'detailed':
        results['warnings'].append("No code snippets found (recommended for detailed case studies)")

    # 7. Markdown formatting check
    formatting_issues = check_markdown_formatting(content)
    if formatting_issues:
        results['issues'].extend(formatting_issues)
        results['passed'] = False

    return results


def print_results(results: Dict):
    """Print validation results in a readable format."""
    print(f"\n{'='*60}")
    print(f"Case Study Validation Results")
    print(f"{'='*60}")
    print(f"File: {results.get('file', 'N/A')}")
    print(f"Format: {results.get('format_type', 'N/A')}")
    print(f"Word Count: {results.get('word_count', 0)}")
    print(f"Status: {'✅ PASSED' if results.get('passed') else '❌ FAILED'}")
    print(f"{'='*60}\n")

    if results.get('issues'):
        print("❌ ISSUES (must fix):")
        for issue in results['issues']:
            print(f"  - {issue}")
        print()

    if results.get('warnings'):
        print("⚠️  WARNINGS (should fix):")
        for warning in results['warnings']:
            print(f"  - {warning}")
        print()

    if results.get('suggestions'):
        print("💡 SUGGESTIONS:")
        for suggestion in results['suggestions']:
            print(f"  - {suggestion}")
        print()


def main():
    """CLI entry point."""
    if len(sys.argv) < 3:
        print("Usage: python3 validate-case-study.py <file-path> <format-type>")
        print("       format-type: 'detailed' or 'concise'")
        sys.exit(1)

    file_path = sys.argv[1]
    format_type = sys.argv[2].lower()

    if format_type not in ['detailed', 'concise']:
        print("Error: format-type must be 'detailed' or 'concise'")
        sys.exit(1)

    results = validate_case_study(file_path, format_type)
    print_results(results)

    # Exit with appropriate code
    sys.exit(0 if results.get('passed') else 1)


if __name__ == '__main__':
    main()
