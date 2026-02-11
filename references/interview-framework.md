# Interview Framework for Case Study Writing

This document provides the complete conditional branching logic, question templates, and exit criteria for conducting progressive interviews during case study development.

## Progressive Disclosure Model

Each interview topic follows a three-tier questioning pattern:

1. **Surface** (1-2 questions): Get the basics and establish context
2. **Depth** (2-3 questions): Understand the "why" and reasoning
3. **Evidence** (1-2 questions): Get specifics, proof, and concrete examples

Continue questioning until exit criteria are met for each topic.

---

## Topic 1: Technical Decisions

### Initial Questions (Surface Level)

1. **"What was the most important technical decision you made on this project?"**
   - Listen for: Architecture choices, technology selection, implementation approaches
   - Red flags: Vague answers like "we used best practices" or generic statements

2. **"What alternatives did you consider?"**
   - Listen for: Specific other options, competitive technologies, different approaches
   - Red flags: "I didn't consider alternatives" or "this was the obvious choice"

3. **"Why did you choose this approach over the alternatives?"**
   - Listen for: Clear reasoning, trade-offs understood, contextual factors
   - Red flags: "Because it's popular" or "everyone uses it"

### Conditional Branching (Depth Level)

**Branch A: IF mentions scalability/performance**
```
User mentions: "needed to scale", "handle traffic", "performance requirements"

Follow-up Questions:
→ "What traffic or user growth were you planning for?"
→ "What metrics validated that this approach worked?"
→ "What benchmarks or load testing did you do?"

Listen for: Specific numbers (requests/second, users, data volume)
Example good answer: "Needed to handle 10k concurrent users, achieved 50ms p95 latency"
Example weak answer: "It's fast" or "performs well"
```

**Branch B: IF mentions new technology/framework**
```
User mentions: "first time using", "learned", "new to the team", "adopted"

Follow-up Questions:
→ "What was the learning curve like? How long to become productive?"
→ "How did you mitigate the risk of using something new?"
→ "What documentation or resources helped you?"

Listen for: Honest assessment, risk mitigation strategies, team considerations
Example good answer: "Took 2 weeks to learn basics, used TypeScript to catch errors early"
Example weak answer: "It was easy" or "no problems"
```

**Branch C: IF mentions refactoring/migration**
```
User mentions: "migrated from", "refactored", "replaced", "upgraded"

Follow-up Questions:
→ "What were the before/after metrics? How did you measure improvement?"
→ "How long did the migration take? Any downtime?"
→ "What was the biggest risk or challenge during migration?"

Listen for: Quantified improvements, migration strategy, risk management
Example good answer: "Migrated over 3 weeks using strangler pattern, reduced bundle size 40%"
Example weak answer: "Made it better" or "no issues"
```

**Branch D: IF mentions architecture choice**
```
User mentions: "microservices", "monolith", "serverless", "event-driven", "REST vs GraphQL"

Follow-up Questions:
→ "What were the specific trade-offs between the options?"
→ "How did you decide which trade-offs were acceptable?"
→ "Looking back, would you make the same choice?"

Listen for: Understanding of trade-offs, thoughtful decision-making, reflection
Example good answer: "Chose monolith for faster iteration, accepted tighter coupling as trade-off"
Example weak answer: "Microservices are better" or vague generalizations
```

**Branch E: IF answer is vague or generic**
```
User says: "we followed best practices", "used standard approach", "nothing special"

Follow-up Questions:
→ "Can you give a specific example with code or concrete details?"
→ "What problem were you solving with this decision?"
→ "What would have happened if you chose differently?"

Goal: Push for specificity and actual technical depth
```

### Code Snippet Follow-Up

After depth questions, always ask:
**"Could you share a representative code snippet that illustrates this decision?"**

Good code snippets:
- 2-10 lines of actual code
- Shows the decision in action
- Includes brief comment explaining why
- Demonstrates technical competence

### Exit Criteria for Technical Decisions

Don't move to the next topic until achieving:

- [ ] **At least 2 specific technical decisions** documented with clear names
- [ ] **Clear reasoning** for each choice (not just "best practice" or "it's popular")
- [ ] **Alternatives considered** or trade-offs explicitly articulated
- [ ] **One concrete example** with code snippet or implementation detail
- [ ] **Measurable outcome** if possible (performance improvement, reduced complexity, etc.)

---

## Topic 2: Design Process

### Initial Questions (Surface Level)

1. **"How did the design evolve from initial concept to final version?"**
   - Listen for: Design iterations, changes over time, evolution
   - Red flags: "Didn't change" or "designed once and built it"

2. **"What user research or feedback influenced the design?"**
   - Listen for: Actual research activities, user testing, feedback loops
   - Red flags: "No user research" or "I just knew what users wanted"

3. **"What design challenges did you encounter?"**
   - Listen for: Real obstacles, constraints, difficult decisions
   - Red flags: "No challenges" or generic problems

### Conditional Branching (Depth Level)

**Branch A: IF mentions user research**
```
User mentions: "interviewed users", "surveys", "analytics", "user testing", "feedback"

Follow-up Questions:
→ "What were the key findings from the research?"
→ "How did those findings change your design?"
→ "How did you validate your assumptions?"

Listen for: Specific insights, data-driven decisions, iteration based on findings
Example good answer: "5 of 8 users couldn't find checkout button, moved it above fold"
Example weak answer: "Users liked it" or vague feedback
```

**Branch B: IF mentions iterations**
```
User mentions: "version 1", "first draft", "revised", "changed", "improved"

Follow-up Questions:
→ "What specifically changed between versions?"
→ "What drove those changes? (feedback, data, constraints?)"
→ "Can you describe what version 1 looked like vs the final version?"

Listen for: Concrete changes, clear drivers, willingness to iterate
Example good answer: "V1 had 3-column layout, analytics showed 70% mobile users, switched to single column"
Example weak answer: "Made it better" or "improved UI"
```

**Branch C: IF mentions accessibility/performance**
```
User mentions: "accessible", "WCAG", "screen readers", "performance", "load time", "responsive"

Follow-up Questions:
→ "What specific accessibility standards did you target?"
→ "What metrics did you track?"
→ "What improvements did you achieve?"

Listen for: Specific standards (WCAG 2.1 AA), actual metrics (Lighthouse score, load time)
Example good answer: "Achieved WCAG 2.1 AA, tested with screen readers, 1.2s load time"
Example weak answer: "Made it accessible" or "it's fast"
```

**Branch D: IF only describes final design**
```
User only talks about: "the final design has...", "features include...", "users can..."

Follow-up Questions:
→ "What was the initial design concept? How did it differ?"
→ "What changed during development and why?"
→ "What surprised you about how users actually used it?"

Goal: Uncover the design journey, not just the destination
```

**Branch E: IF mentions design systems/components**
```
User mentions: "design system", "component library", "Material UI", "shadcn", "Tailwind"

Follow-up Questions:
→ "Did you customize the components or use them as-is?"
→ "What decisions did you make about consistency vs customization?"
→ "How did the design system speed up or constrain your work?"

Listen for: Thoughtful use of tools, customization decisions, trade-offs
Example good answer: "Used shadcn base, customized colors for brand, saved 2 weeks on components"
Example weak answer: "Just used Material UI" with no details
```

### Exit Criteria for Design Process

Don't move to the next topic until achieving:

- [ ] **Initial concept vs final design** described (what changed and why)
- [ ] **User research, feedback, or testing** mentioned with specific findings
- [ ] **At least one design iteration** explained with clear driver
- [ ] **Visual or functional design challenge** overcome
- [ ] **Design rationale** articulated (not just "looks good")

---

## Topic 3: Business Impact

### Initial Questions (Surface Level)

1. **"What problem did this project solve for users or the business?"**
   - Listen for: Clear problem statement, stakeholder pain points, user needs
   - Red flags: Vague goals or "wanted a website"

2. **"What metrics improved as a result?"**
   - Listen for: Specific KPIs, quantifiable outcomes
   - Red flags: "It went well" or no metrics

3. **"What was the client or stakeholder reaction?"**
   - Listen for: Feedback, testimonials, continued engagement
   - Red flags: "They were happy" with no details

### Conditional Branching (Depth Level)

**Branch A: IF mentions metrics**
```
User mentions: "increased", "decreased", "improved", "conversion rate", "revenue", "users"

Follow-up Questions:
→ "What were the before/after numbers?"
→ "How long did it take to see these results?"
→ "How did you measure and track these metrics?"

Listen for: Specific numbers, timeframes, measurement methodology
Example good answer: "Conversion increased from 2.1% to 3.8% over 2 months, tracked via Google Analytics"
Example weak answer: "Things got better" or percentages without context
```

**Branch B: IF no metrics mentioned**
```
User says: "went well", "successful", "liked it", but no numbers

Follow-up Questions:
→ "How did you measure success for this project?"
→ "What qualitative feedback did you receive?"
→ "Can you share specific quotes or examples from users/stakeholders?"

Goal: Extract either quantitative metrics OR rich qualitative data
Listen for: Specific feedback, testimonials, repeated use, referrals
Example good answer: "Client said: 'This cut our admin time in half', they referred 2 other clients"
Example weak answer: "Everyone was happy" with no specifics
```

**Branch C: IF mentions user feedback**
```
User mentions: "users said", "feedback", "reviews", "comments", "testimonials"

Follow-up Questions:
→ "Can you share specific quotes or examples?"
→ "What were the most common themes in the feedback?"
→ "Did any feedback surprise you?"

Listen for: Direct quotes, specific themes, insights gained
Example good answer: "'Finally a booking system that works' was most common comment, 4.7/5 average rating"
Example weak answer: "Users liked it" with no quotes
```

**Branch D: IF vague business goals**
```
User says: "improve the business", "help the company", "better experience" without specifics

Follow-up Questions:
→ "Who was the primary user or stakeholder?"
→ "What specific pain point were they experiencing?"
→ "How did they operate before your solution? What changed after?"

Goal: Ground vague goals in concrete user stories
```

**Branch E: For Ad Campaigns Specifically**
```
IF project involved ads, paid campaigns, or marketing:

Follow-up Questions:
→ "What was the ROAS (Return on Ad Spend) or conversion rate?"
→ "What audience targeting strategy performed best?"
→ "Did you run A/B tests? What creative variations won?"
→ "What was the cost per acquisition?"

Listen for: Specific campaign metrics, testing rigor, optimization approach
Example good answer: "3.2x ROAS, carousel ads outperformed static by 40%, CPA dropped from $45 to $28"
Example weak answer: "Ads performed well" with no numbers
```

### Estimating Impact Without Hard Metrics

Sometimes users don't have concrete metrics. Help them estimate:

**Time saved estimation**:
- "If this saves 1 hour per day, that's 260 hours per year"
- "That's about 6 weeks of work saved annually"

**Cost reduction estimation**:
- "What was the manual process cost? (hourly rate × hours)"
- "What does automation save? (cost before - cost after)"

**User satisfaction proxies**:
- "How many support tickets decreased?"
- "Did users adopt it quickly? What percentage using it?"
- "Any retention or churn changes?"

### Exit Criteria for Business Impact

Don't move to the next topic until achieving:

- [ ] **Primary problem** clearly stated with user/stakeholder context
- [ ] **At least 2 quantifiable metrics** OR rich qualitative data with quotes
- [ ] **Stakeholder/user reaction** documented
- [ ] **Timeline context** (how long to see results, when measured)
- [ ] **Business value** articulated (ROI, cost savings, revenue, satisfaction)

---

## Topic 4: Challenges & Learning

### Initial Questions (Surface Level)

1. **"What was the biggest challenge you faced on this project?"**
   - Listen for: Genuine obstacles, not trivial issues
   - Red flags: "No challenges" or "everything went smoothly"

2. **"How did you overcome it?"**
   - Listen for: Problem-solving approach, iteration, collaboration
   - Red flags: "Just figured it out" without details

3. **"What would you do differently knowing what you know now?"**
   - Listen for: Self-awareness, reflection, growth mindset
   - Red flags: "Nothing, it was perfect"

### Conditional Branching (Depth Level)

**Branch A: IF technical challenge**
```
User mentions: "bug", "performance issue", "integration problem", "technical debt", "architecture problem"

Follow-up Questions:
→ "What solutions did you try first? Why didn't they work?"
→ "What ultimately worked? How did you figure it out?"
→ "What did you learn from this that you'll use next time?"

Listen for: Iteration, debugging process, learning
Example good answer: "Tried caching, then query optimization, finally indexed foreign keys - reduced query from 2s to 50ms, learned to profile first"
Example weak answer: "Fixed the bug" without process details
```

**Branch B: IF resource/timeline challenge**
```
User mentions: "tight deadline", "limited budget", "small team", "not enough time"

Follow-up Questions:
→ "How did you prioritize features? What framework did you use?"
→ "What did you decide to scope out or cut?"
→ "Looking back, did you cut the right things?"

Listen for: Prioritization frameworks (MoSCoW, Value/Effort), strategic thinking
Example good answer: "Used MoSCoW method, cut admin panel to MVP launch on time, added post-launch"
Example weak answer: "Worked faster" or "did everything"
```

**Branch C: IF team/stakeholder challenge**
```
User mentions: "disagreement", "stakeholder pushback", "team conflict", "communication issues"

Follow-up Questions:
→ "How did you align everyone? What approach worked?"
→ "What communication strategies did you use?"
→ "How did you balance different perspectives?"

Listen for: Diplomacy, communication skills, consensus building
Example good answer: "Created prototype to demo both approaches, stakeholders saw trade-offs clearly, reached decision together"
Example weak answer: "Convinced them I was right" without details
```

**Branch D: IF says "no major challenges"**
```
User claims everything went smoothly

Follow-up Questions:
→ "What would you optimize if you did this project again?"
→ "What took longer than expected?"
→ "What aspect of the project was most difficult, even if you succeeded?"

Goal: Everyone has challenges; help them recognize and articulate them
```

**Branch E: IF mentions learning/growth**
```
User mentions: "learned", "first time", "new skill", "grew", "improved"

Follow-up Questions:
→ "What specific skills did you develop?"
→ "How will you apply this learning to future projects?"
→ "What resources or mentors helped you learn?"

Listen for: Concrete skills, growth mindset, resourcefulness
Example good answer: "Learned WebSocket architecture, will use for real-time features going forward, Kent C. Dodds courses helped"
Example weak answer: "Got better at coding" without specifics
```

### Exit Criteria for Challenges & Learning

Don't move to the next topic until achieving:

- [ ] **One major challenge** with specific details (not trivial)
- [ ] **Solution approach** described with process steps
- [ ] **Outcome** of solution (did it work? what was the result?)
- [ ] **Learning or reflection** included with future application
- [ ] **Self-awareness** demonstrated (not claiming perfection)

---

## Question Templates by Role Focus

### For Fullstack Developers

**Technical Deep Dives**:
- "How did you structure the API and data flow?"
- "What database design decisions were critical? Any normalization trade-offs?"
- "How did you handle state management on the frontend?"
- "What testing strategy did you implement? (unit, integration, e2e)"
- "How did you optimize for performance across the stack?"

**Architecture Focus**:
- "How did you separate concerns between frontend and backend?"
- "What authentication and authorization approach did you use?"
- "How did you handle API versioning and backwards compatibility?"

### For Frontend Designers

**Design + Implementation**:
- "How did you translate design mockups to components?"
- "What accessibility considerations shaped the design?"
- "How did you optimize for mobile vs desktop experiences?"
- "What design system or component library did you use?"
- "How did you measure and improve performance?"

**Visual + Interaction Design**:
- "What design tools did you use? (Figma, Sketch, etc.)"
- "How did you approach animations and micro-interactions?"
- "What typography and color systems did you establish?"
- "How did you balance aesthetics with usability?"

### For Digital Strategy

**Strategic Focus**:
- "What were the conversion goals and how did you structure the funnel?"
- "How did you define and prioritize the user journey?"
- "What analytics did you track to measure success?"
- "How did content strategy influence the design?"
- "What A/B tests or experiments did you run?"

**Business Alignment**:
- "How did this project align with broader business goals?"
- "What KPIs did stakeholders care about most?"
- "How did you balance short-term wins with long-term strategy?"

### For Ad Campaign Management

**Campaign Specifics**:
- "What was the campaign objective? (awareness, conversions, engagement)"
- "How did you target and segment audiences?"
- "What creative variations did you test?"
- "What was the ROAS (Return on Ad Spend)?"
- "How did you optimize the campaign during flight?"

**Platform + Strategy**:
- "Which platforms performed best? (Meta, Google, TikTok, etc.)"
- "What bidding strategy did you use?"
- "How did you allocate budget across platforms?"
- "What was your attribution model?"

---

## General Interview Techniques

### Building on Previous Answers

Always reference earlier responses when asking follow-up questions:

❌ **Bad**: "What technologies did you use?"
✅ **Good**: "You mentioned using React earlier. Why did you choose React over Vue or Svelte?"

❌ **Bad**: "Tell me about challenges."
✅ **Good**: "Given that you were migrating from a monolith to microservices, what was the biggest challenge during that transition?"

### Handling Incomplete Answers

If a user gives a vague or incomplete answer:

1. **Acknowledge**: "That makes sense..."
2. **Probe gently**: "Can you give me a specific example?"
3. **Offer context**: "For instance, did you compare React to Vue, or was React already decided?"

### When to Push vs When to Move On

**Push for more detail when**:
- Answer is vague or generic
- No concrete examples provided
- Technical depth is missing
- Can't distinguish this project from others

**Move on when**:
- User has given rich, specific details
- Exit criteria for topic are met
- User seems uncomfortable or blocked
- Simple project doesn't warrant deeper exploration

### Adapting to Project Complexity

**Simple projects** (side projects, MVPs, short timelines):
- Fewer follow-up questions needed
- Focus on 1-2 key technical decisions
- Emphasize learning and iteration

**Complex projects** (enterprise, long timelines, large teams):
- Deeper exploration warranted
- Multiple technical decisions to document
- More focus on collaboration and architecture

---

## Red Flags and How to Address Them

### Red Flag: "No challenges"

**Response**: "Every project has trade-offs or constraints. What aspect took longest or was most difficult, even if you succeeded?"

### Red Flag: Generic tech buzzwords

**Response**: "When you say 'microservices', can you describe the specific services you created and how they communicated?"

### Red Flag: No metrics or outcomes

**Response**: "Even without hard data, how did you know the project succeeded? What feedback did you receive?"

### Red Flag: Claiming perfection

**Response**: "What would you optimize if you did this again? What could be improved?"

### Red Flag: Only listing features

**Response**: "Instead of what you built, tell me why you built it that way. What alternatives did you consider?"

---

## Interview Pacing

### Recommended Time per Topic

- **Technical Decisions**: 5-10 minutes (most technical depth)
- **Design Process**: 3-7 minutes (varies by role)
- **Business Impact**: 3-5 minutes (get metrics fast)
- **Challenges & Learning**: 3-5 minutes (one good challenge is enough)

**Total interview time**: 15-30 minutes depending on project complexity

### Signs You're Going Too Deep

- User is repeating themselves
- Answers becoming shorter and less detailed
- User asks "is this enough?"
- Reaching 45+ minutes total interview time

### Signs You Need More Depth

- Can't distinguish this project from any other project
- No specific technical examples or code
- No concrete metrics or outcomes
- No evidence of problem-solving or learning

---

## Final Checklist

Before ending the interview, ensure you have:

**Technical**:
- [ ] 2+ specific technical decisions with rationale
- [ ] At least 1 code snippet or concrete implementation detail
- [ ] Understanding of tech stack and why it was chosen

**Design**:
- [ ] Design evolution (initial → final) described
- [ ] User research or feedback mentioned
- [ ] At least 1 design challenge overcome

**Impact**:
- [ ] 2+ quantifiable metrics OR rich qualitative data
- [ ] Clear problem statement
- [ ] Stakeholder/user reaction

**Challenges**:
- [ ] 1 major challenge with solution process
- [ ] Learning or growth articulated
- [ ] Honest reflection (not claiming perfection)

If any checklist items are missing, return to that topic with targeted questions.
