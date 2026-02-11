# Portfolio Case Study Writer

> A Claude Code skill/plugin for generating portfolio-worthy case studies through structured interviews

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](https://github.com/anthropics/claude-code)

## Overview

This Claude Code skill conducts progressive interviews to help fullstack developers, frontend designers, and digital strategists create compelling case studies that effectively showcase technical expertise and business value.

**Key Features:**
- 📋 **Progressive Interview System** - Adaptive questioning with conditional branching across 4 core topics
- 📊 **Dual-Format Output** - Generates both detailed (1500-2500 words) and concise (500-800 words) versions from a single interview
- 🚀 **PRD Auto-Extraction** - Automatically parses project documents to jumpstart interviews
- ✅ **Quality Validation** - Built-in checks for metrics, AI-tell vocabulary, and technical specificity
- 📚 **Comprehensive Guides** - 2,929 lines of expert documentation across 4 reference files
- 🛠️ **Automation Scripts** - Python/Bash utilities for extraction, validation, and formatting

## Installation

### As a Claude Code Skill

1. **Download the skill:**
   ```bash
   cd ~/.openclaw/workspace/skills
   git clone https://github.com/unobtuse/portfolio-case-study-writer.git
   ```

2. **Make scripts executable:**
   ```bash
   cd portfolio-case-study-writer
   chmod +x scripts/*.py scripts/*.sh
   ```

3. **Verify Python 3 is installed:**
   ```bash
   python3 --version  # Should be 3.7 or higher
   ```

### As a Claude Code Plugin

Install using Claude Code's plugin system:
```bash
cc plugin install unobtuse/portfolio-case-study-writer
```

## Quick Start

### Trigger the Skill

Simply ask Claude:
- *"Write a case study for my e-commerce project"*
- *"Create portfolio content from this app"*
- *"Turn this PRD into a case study"*
- *"Document this project for my portfolio"*

### Upload a PRD (Optional)

Upload a project summary or PRD markdown file, and the skill will automatically extract:
- Project name and description
- Tech stack
- Timeline
- Key features
- Success criteria

### Complete the Interview

The skill conducts a structured 4-topic interview:

1. **Technical Decisions** - Architecture, stack choices, trade-offs
2. **Design Process** - Research, iterations, UX/UI decisions
3. **Business Impact** - Metrics, ROI, stakeholder feedback
4. **Challenges & Learning** - Obstacles overcome, growth demonstrated

### Receive Both Formats

- **Detailed version** (1500-2500 words): For portfolio websites, blog posts, hiring managers
- **Concise version** (500-800 words): For LinkedIn, quick-scan resumes, client proposals

## File Structure

```
portfolio-case-study-writer/
├── .claude-plugin/
│   └── plugin.json              # Plugin metadata
├── SKILL.md                     # Main skill workflow (465 lines)
├── references/                  # Deep expertise (1,747 lines)
│   ├── interview-framework.md   # Conditional branching logic
│   ├── storytelling-patterns.md # Narrative structures & hooks
│   ├── technical-writing-guide.md # Explaining tech decisions
│   └── metrics-framework.md     # Quantifying impact
├── templates/                   # Output structures (200 lines)
│   ├── detailed-case-study.md   # Full format template
│   ├── concise-case-study.md    # Quick-scan template
│   └── interview-state.json     # Content model
├── scripts/                     # Automation utilities (517 lines)
│   ├── extract-project-info.py  # Parse PRDs/summaries
│   ├── validate-case-study.py   # Quality assurance
│   └── format-markdown.sh       # Markdown cleanup
├── .gitignore
└── README.md
```

**Total:** 11 files, 2,929 lines of expert documentation

## How It Works

### The 5-Stage Workflow

#### Stage 1: Input Processing
- Reads uploaded PRD or project summary (if provided)
- Extracts key information automatically
- Presents findings for confirmation

#### Stage 2: Initial Context Gathering
- 3-4 foundational questions via `AskUserQuestion`
- Establishes project basics: name, role, timeline, tech stack

#### Stage 3: Progressive Interviewing
**Technical Decisions:**
- Initial questions about architecture and stack
- Conditional branches based on answers:
  - IF mentions scalability → Ask about traffic metrics
  - IF mentions new technology → Ask about learning curve
  - IF mentions refactoring → Ask about before/after metrics

**Design Process:**
- Evolution from concept to final design
- User research and feedback
- Iterations and rationale

**Business Impact:**
- Problem statement and stakeholders
- Quantifiable metrics (conversion, revenue, time saved)
- Qualitative feedback and testimonials

**Challenges & Learning:**
- Biggest obstacles encountered
- Solutions and problem-solving approach
- Reflection and growth demonstrated

#### Stage 4: Content Generation
- Analyzes all interview data
- Identifies 3-5 compelling story elements
- Populates both templates simultaneously
- Applies consistent formatting

#### Stage 5: Validation & Delivery
- Runs quality checks:
  - Word count in target range
  - 2+ quantifiable metrics present
  - No AI-tell vocabulary (delve, leverage, seamless, etc.)
  - Technical specificity verified
- Presents both versions
- Offers refinement based on feedback

## Script Usage

### Extract Project Information from PRD

```bash
python3 scripts/extract-project-info.py project-summary.md
```

**Output:** JSON with project name, tech stack, timeline, features, stakeholders

### Validate Case Study Quality

```bash
python3 scripts/validate-case-study.py case-study.md detailed
```

**Checks:**
- Word count (1500-2500 for detailed, 500-800 for concise)
- Required sections present
- Metrics included
- AI-tell vocabulary detection
- Technical specificity

### Format Markdown

```bash
bash scripts/format-markdown.sh case-study.md
```

**Operations:**
- Remove trailing whitespace
- Normalize paragraph spacing
- Fix heading spacing
- Check for placeholder links
- Validate code blocks

## Reference Guides

### Interview Framework (482 lines)
Complete conditional branching logic for all 4 interview topics:
- Progressive disclosure model (Surface → Depth → Evidence)
- Conditional branching rules for each topic
- Question templates by role (fullstack, designer, strategist, ad campaigns)
- Exit criteria ensuring quality thresholds

### Storytelling Patterns (422 lines)
Narrative structures and techniques:
- Core frameworks: Problem-Solution-Impact, Hero's Journey, Before-After
- 5 opening hook patterns (Shocking Stat, Stakes Statement, Bold Claim, etc.)
- Sustaining engagement through specificity and mini-cliffhangers
- 4 conclusion frameworks with examples

### Technical Writing Guide (423 lines)
Best practices for explaining technical decisions:
- Decision framework (What, Why, Alternatives, Trade-offs, Results)
- Code snippet best practices
- Architecture description patterns
- Balancing jargon with accessibility
- Writing for multiple audience levels

### Metrics Framework (420 lines)
Quantifying impact when "there are no metrics":
- Metrics by project category (web, design, strategy, ads)
- Quantifying qualitative outcomes
- Estimation methods without direct measurement
- Before/after comparison formats
- Contextualizing numbers effectively

## Target Audience

**Primary audiences for generated case studies:**
- **Hiring Managers** - Want technical depth, collaborative process, problem-solving
- **Freelance Clients** - Need business value, ROI, clear outcomes
- **Recruiters** - Require scannable format with key metrics

**Supported specializations:**
- Fullstack development
- Frontend design and UX
- Digital strategy
- Ad campaign management

## Example Output Quality

### Good Indicators ✅
- Specific technical decisions with clear rationale
- Quantifiable metrics (%, multipliers, dollars, time saved)
- Concrete before/after comparisons
- Honest challenges and learnings
- Active voice with personality
- Audience-appropriate depth

### Poor Indicators ❌
- Vague descriptions ("worked on features")
- No metrics or evidence
- Only lists technologies without context
- No challenges mentioned
- Generic AI-sounding language
- Promotional buzzwords

## Advanced Features

### Progressive Disclosure Design
- **SKILL.md** (~3,000 words): Core workflow always loaded
- **references/** (1,747 lines): Loaded on demand when needed
- **scripts/**: Executed without loading into context
- Result: Efficient context usage, scales to any project complexity

### Audience Optimization
- **For Clients:** Emphasize business outcomes, ROI language, problem-solving
- **For Hiring Managers:** Lead with technical sophistication, show collaboration, highlight learning
- **Dual Formats:** Same interview data, optimized for each audience automatically

### Quality Assurance Pipeline
1. **Content Validation** - Metrics present, sections complete
2. **Language Check** - AI-tell vocabulary flagged
3. **Technical Depth** - Specific technologies named, not vague terms
4. **Formatting** - Proper markdown, no placeholders
5. **Completeness** - Exit criteria met for all interview topics

## Contributing

Contributions are welcome! Areas for enhancement:
- Additional reference guides for specific domains
- More validation rules in `validate-case-study.py`
- Export formats (PDF, HTML, Notion, etc.)
- Integration with portfolio platforms
- Multilingual support

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

Built with [Claude Code](https://github.com/anthropics/claude-code) by Anthropic.

---

**Author:** [unobtuse](https://github.com/unobtuse)
**Repository:** [portfolio-case-study-writer](https://github.com/unobtuse/portfolio-case-study-writer)
**Issues:** [Report a bug or request a feature](https://github.com/unobtuse/portfolio-case-study-writer/issues)

*Generate case studies that land interviews and win clients.* 🚀
