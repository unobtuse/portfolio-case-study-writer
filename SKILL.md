---
name: portfolio-case-study-writer
description: This skill should be used when the user asks to "write a case study", "create a case study", "document this project for my portfolio", "turn this PRD into a case study", "help me write up this project", "generate portfolio content", or needs to showcase technical work. Conducts structured interview covering technical decisions, design process, business impact, and challenges overcome. Generates both detailed (1500-2500 words) and concise (500-800 words) markdown case studies optimized for freelance clients and hiring managers.
metadata:
  openclaw:
    emoji: "📝"
    requires:
      bins: ["python3"]
---

# Portfolio Case Study Writer

Generate portfolio-worthy case studies through structured interviewing. This skill conducts progressive interviews to gather comprehensive information about projects, then produces both detailed and concise markdown case studies optimized for different audiences.

## Target Audience

**Primary audiences**:
- **Hiring managers**: Want technical depth, collaborative process, problem-solving skills
- **Freelance clients**: Need business value, ROI, problem-solving capabilities
- **Recruiters**: Require scannable format with key metrics and outcomes

**Specializations supported**:
- Fullstack development
- Frontend design and UX
- Digital strategy
- Ad campaign management

## Workflow Overview

The case study generation process follows five stages:

1. **Input Processing** - Read and extract information from uploaded PRDs or project summaries
2. **Initial Context Gathering** - Establish project fundamentals through targeted questions
3. **Progressive Interviewing** - Conduct four-topic deep dive with conditional branching
4. **Content Generation** - Produce both detailed and concise formats from shared content model
5. **Validation & Delivery** - Quality check and present both versions

---

## Stage 1: Input Processing

### If File Uploaded

When a user provides a PRD, project summary, or project documentation:

1. **Read the file** using the Read tool
2. **Extract key information** by running the extraction script:
   ```bash
   python3 scripts/extract-project-info.py [file-path]
   ```
3. **Store extracted data** in a working note for reference throughout the interview
4. **Present extracted information** to the user for confirmation:
   - Project name
   - Tech stack identified
   - Timeline mentions
   - Key features listed
   - Success criteria noted
5. **Ask for corrections**: "I've extracted this information from your document. Is this accurate, or would you like to correct anything?"

### If No File Uploaded

Proceed directly to Stage 2: Initial Context Gathering.

---

## Stage 2: Initial Context Gathering

Use AskUserQuestion to establish foundational information. Ask 3-4 questions to set context.

**Question 1: Project Basics**
- Question: "What is the project name and a one-sentence description?"
- Header: "Project"
- Options: (Text input from user)

**Question 2: Role & Team**
- Question: "What was your role, and what was the team structure?"
- Header: "Role"
- Options:
  - "Solo developer/designer (I handled everything)"
  - "Lead role (managed a small team)"
  - "Contributor (part of larger team)"
  - "Hybrid (technical + design + strategy)"

**Question 3: Timeline**
- Question: "What was the project timeline?"
- Header: "Timeline"
- Options: (Text input: e.g., "3 months", "Jan 2025 - Mar 2025")

**Question 4: Primary Technologies**
- Question: "What were the core technologies or tools you used?"
- Header: "Tech Stack"
- Options: (Text input: e.g., "React, Node.js, PostgreSQL, Figma")

**Store all responses** in working notes to reference throughout the interview.

---

## Stage 3: Progressive Interviewing

Conduct four topic deep dives with conditional branching. Each topic follows the pattern: **Surface → Depth → Evidence**.

For detailed conditional branching logic, consult **`references/interview-framework.md`**.

### Topic 1: Technical Decisions

**Goal**: Uncover architectural choices, engineering challenges, and technical trade-offs.

**Initial Questions** (2-3):
1. "What was the most important technical decision you made on this project?"
2. "What alternatives did you consider?"
3. "Why did you choose this approach over the alternatives?"

**Conditional Branching**:
- **IF mentions scalability** → Ask: "What traffic or user growth were you planning for? What metrics validated this approach?"
- **IF mentions new technology/framework** → Ask: "What was the learning curve? How did you mitigate adoption risk?"
- **IF mentions refactoring/migration** → Ask: "What were the before/after metrics? How long did it take?"
- **IF mentions architecture choice** → Ask: "What were the specific trade-offs between options?"
- **IF answer is vague** → Ask: "Can you give a specific example with code or concrete details?"

**Follow-up for code snippets**:
- "Could you share a representative code snippet that illustrates this decision?"

**Exit criteria** (don't move on until achieved):
- [ ] At least 2 specific technical decisions documented
- [ ] Clear reasoning for each choice (not just "best practice")
- [ ] Alternatives considered or trade-offs articulated
- [ ] One concrete code example or implementation detail

### Topic 2: Design Process

**Goal**: Document UX/UI decisions, user research, and design iteration.

**Initial Questions**:
1. "How did the design evolve from initial concept to final version?"
2. "What user research or feedback influenced the design?"
3. "What design challenges did you encounter?"

**Conditional Branching**:
- **IF mentions user research** → Ask: "What were the key findings? How did you validate assumptions?"
- **IF mentions iterations** → Ask: "What specifically changed between versions and why?"
- **IF mentions accessibility/performance** → Ask: "What metrics did you track? What improvements did you achieve?"
- **IF only describes final design** → Ask: "What was the initial concept? Why did it change?"

**Exit criteria**:
- [ ] Initial concept vs final design described
- [ ] User research, feedback, or testing mentioned
- [ ] At least one design iteration explained
- [ ] Visual or functional design challenge overcome

### Topic 3: Business Impact

**Goal**: Quantify results, demonstrate value delivered, and capture stakeholder response.

**Initial Questions**:
1. "What problem did this project solve for users or the business?"
2. "What metrics improved as a result?" (users, revenue, conversion, time saved, etc.)
3. "What was the client or stakeholder reaction?"

**Conditional Branching**:
- **IF mentions metrics** → Ask: "What were the before/after numbers? How long to see results?"
- **IF no metrics mentioned** → Ask: "How did you measure success? What qualitative feedback did you receive?"
- **IF mentions user feedback** → Ask: "Can you share specific quotes or examples?"
- **IF vague business goals** → Ask: "Who was the primary user/stakeholder? What pain point were they experiencing?"

**For ad campaigns specifically**:
- Ask about ROAS (Return on Ad Spend), conversion rates, cost per acquisition
- Ask about A/B testing results, audience targeting effectiveness
- Ask about creative variations and performance differences

**Exit criteria**:
- [ ] Primary problem clearly stated
- [ ] At least 2 quantifiable metrics OR rich qualitative data
- [ ] Stakeholder/user reaction documented
- [ ] Timeline context (how long to see results)

### Topic 4: Challenges & Learning

**Goal**: Show problem-solving ability, adaptability, and professional growth.

**Initial Questions**:
1. "What was the biggest challenge you faced on this project?"
2. "How did you overcome it?"
3. "What would you do differently knowing what you know now?"

**Conditional Branching**:
- **IF technical challenge** → Ask: "What solutions did you try? What ultimately worked? What did you learn?"
- **IF resource/timeline challenge** → Ask: "How did you prioritize? What did you scope out?"
- **IF team/stakeholder challenge** → Ask: "How did you align everyone? What communication approach worked?"
- **IF says "no major challenges"** → Ask: "What would you optimize if you did it again? What could be improved?"

**Exit criteria**:
- [ ] One major challenge with specific details
- [ ] Solution approach described
- [ ] Outcome of solution (did it work?)
- [ ] Learning or reflection included

---

## Stage 4: Content Generation

### Pre-Generation Analysis

Before generating case studies, review all interview data and:

1. **Identify compelling story elements**: Select 3-5 most impactful moments
2. **Select best metrics**: Prioritize quantifiable outcomes that demonstrate value
3. **Choose narrative structure**: Consult **`references/storytelling-patterns.md`** for appropriate framework

### Dual-Format Strategy

Generate **both formats simultaneously** from the same interview data using a shared content model.

**Content Model Structure**:
```json
{
  "core_data": {
    "project_name": "",
    "one_line_description": "",
    "role": "",
    "timeline": "",
    "tech_stack": [],
    "problem_statement": "",
    "key_metrics": []
  },
  "technical_decisions": [
    {
      "decision": "",
      "context": "",
      "alternatives": [],
      "rationale": "",
      "code_snippet": "",
      "outcome": ""
    }
  ],
  "design_process": {
    "initial_concept": "",
    "research_findings": "",
    "iterations": [],
    "final_rationale": ""
  },
  "challenges": [
    {
      "challenge": "",
      "attempts": "",
      "solution": "",
      "learning": ""
    }
  ],
  "impact": {
    "quantitative_metrics": [],
    "qualitative_feedback": "",
    "business_value": ""
  }
}
```

### Template Population

**For Detailed Version** (1500-2500 words):
- Use **ALL content** from the model
- Expand each technical decision with full context
- Include all design iterations
- Document multiple challenges
- Comprehensive metrics tables
- Full reflection section

Use template: **`templates/detailed-case-study.md`**

**For Concise Version** (500-800 words):
- Use **SAME core data**
- Select **top 1 technical decision** (most impactful)
- Summarize design process in 1 paragraph
- Select **top 1 challenge** (best problem-solving example)
- Core metrics only (3-5 maximum)
- Brief learning statement

Use template: **`templates/concise-case-study.md`**

### Content Prioritization Rules

When selecting content for the concise version:

- **Technical**: Choose decision with most measurable impact
- **Design**: Focus on outcome, not detailed process
- **Challenges**: Choose challenge demonstrating strongest problem-solving
- **Metrics**: Business metrics > technical metrics

### Output Generation

1. **Populate both templates** with interview data
2. **Format markdown** by running:
   ```bash
   bash scripts/format-markdown.sh [output-file]
   ```
3. **Store both versions** with descriptive filenames:
   - `{project-name}-case-study-detailed.md`
   - `{project-name}-case-study-concise.md`

---

## Stage 5: Validation & Delivery

### Run Validation Script

Before presenting case studies to the user, validate quality:

```bash
python3 scripts/validate-case-study.py detailed-case-study.md detailed
python3 scripts/validate-case-study.py concise-case-study.md concise
```

**Validation checks**:
- Word count in target range
- Required sections present
- At least 2 quantifiable metrics
- No AI-tell vocabulary (delve, leverage, seamless, robust, groundbreaking, etc.)
- Technical specificity (no vague claims like "modern framework")
- Proper markdown formatting

**If validation fails**:
- Review issues and warnings
- Revise content to address problems
- Re-run validation until passed

### Present to User

Once validation passes, present both case studies:

1. **Show detailed version first** with full context
2. **Follow with concise version** for comparison
3. **Explain usage recommendations**:
   - **Detailed**: Portfolio website, blog posts, Medium articles, GitHub project READMEs, hiring manager deep dives
   - **Concise**: Portfolio homepage, LinkedIn featured section, project carousels, quick-scan resumes, client proposals

4. **Offer refinement**: "Would you like me to adjust anything? I can:
   - Add more technical depth
   - Emphasize different metrics
   - Adjust tone for specific audience
   - Include additional sections"

5. **Provide export options**:
   - Markdown (source files)
   - HTML (for web publishing)
   - PDF (via Pandoc if available)

---

## Best Practices

### Writing Quality

- **Use active voice** and specific action verbs (built, designed, optimized, implemented)
- **Include code snippets** where relevant (2-10 lines max)
- **Name actual technologies** (not "modern frameworks" or "industry-standard tools")
- **Balance technical depth with readability** (explain jargon)
- **Show personality and opinion** (avoid sterile AI tone)

### Audience Optimization

**For Freelance Clients:**
- Emphasize **business outcomes first** (ROI, revenue, growth)
- Use **ROI language** (returned $X for every $Y invested)
- Include **client testimonial** if available
- Focus on **problem-solving** and timely delivery

**For Hiring Managers:**
- Lead with **technical sophistication** (architecture, scalability, best practices)
- Show **collaborative process** (team work, code reviews, mentorship)
- Highlight **learning and adaptation** (new technologies, process improvements)
- Demonstrate **software engineering principles** (testing, documentation, maintainability)

### Common Pitfalls to Avoid

❌ **Generic descriptions**: "Built a web app" → ✅ "Built a React SPA with Node.js API serving 10k+ users"
❌ **Missing metrics**: "Improved performance" → ✅ "Reduced page load time from 4s to 800ms (80% improvement)"
❌ **Tech stack listing without context**: "Used React, Node, PostgreSQL" → ✅ "Chose React for component reusability and Node.js for real-time features via WebSockets"
❌ **No challenges documented**: Shows lack of depth or honesty
❌ **Promotional language**: "groundbreaking", "cutting-edge", "revolutionary"

---

## Additional Resources

For detailed guidance on specific aspects of case study writing, consult the reference files:

### Reference Files

- **`references/interview-framework.md`** - Complete conditional branching logic for all four interview topics, exit criteria, question templates by role
- **`references/storytelling-patterns.md`** - Narrative structures (hero's journey, problem-solution-impact), opening hooks, conclusion frameworks
- **`references/technical-writing-guide.md`** - How to explain technical decisions clearly, code snippet best practices, architecture diagrams, balancing jargon
- **`references/metrics-framework.md`** - Types of metrics for different projects, quantifying qualitative outcomes, before/after formats, estimating impact without hard data

### Template Files

- **`templates/detailed-case-study.md`** - Complete structure with all sections and variable placeholders
- **`templates/concise-case-study.md`** - Streamlined structure for quick-scan format
- **`templates/interview-state.json`** - Content model structure for organizing interview data

### Script Files

- **`scripts/extract-project-info.py`** - Parse PRD/summary files for automatic data extraction
- **`scripts/validate-case-study.py`** - Quality assurance checks before delivery
- **`scripts/format-markdown.sh`** - Ensure consistent markdown formatting

---

## Examples

### Example Trigger Phrases

When users say:
- "Write a case study for my e-commerce project"
- "Help me document this app for my portfolio"
- "Turn this PRD into a case study"
- "Create portfolio content from this project"
- "I need to showcase this work for job applications"

This skill activates and begins the workflow.

### Example Output Quality

**Good case study indicators**:
- ✅ Specific technical decisions with clear rationale
- ✅ Quantifiable metrics (%, x, $, user counts)
- ✅ Concrete before/after comparisons
- ✅ Honest challenges and learnings
- ✅ Active voice and personality
- ✅ Audience-appropriate depth

**Poor case study indicators**:
- ❌ Vague descriptions ("worked on features")
- ❌ No metrics or evidence
- ❌ Only lists technologies without context
- ❌ No challenges mentioned
- ❌ Generic AI-sounding language
- ❌ Promotional buzzwords

---

## Notes

**State Management**: For complex interviews spanning multiple conversation turns, maintain context by taking notes of all responses. Reference previous answers when asking follow-up questions to show continuity.

**Flexibility**: Adapt interview depth based on project complexity. Simple projects may require fewer follow-up questions; complex projects warrant deeper exploration.

**User Control**: Always let users guide the depth and focus. If they want to skip a topic or move quickly, respect that preference while ensuring minimum quality thresholds are met.

**Iterative Refinement**: After delivering case studies, be prepared to iterate. Users often want adjustments after seeing initial output, especially around technical depth, metric emphasis, or tone.
