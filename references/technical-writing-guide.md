# Technical Writing Guide for Case Studies

This guide provides best practices for explaining technical decisions, code examples, and architecture in case studies that balance depth with accessibility.

## Core Principles

1. **Specificity builds credibility** - Name technologies, versions, specific choices
2. **Context explains decisions** - Show why, not just what
3. **Trade-offs demonstrate maturity** - Nothing is perfect; show you understand costs
4. **Code should illuminate, not obscure** - Use snippets that teach
5. **Assume smart, not expert** - Explain jargon without dumbing down

---

## Writing About Technical Decisions

### Decision Framework

Every technical decision should answer these questions:

1. **What did you choose?** (The decision)
2. **What were the alternatives?** (Options considered)
3. **Why did you choose this?** (Rationale and context)
4. **What trade-offs did you accept?** (Costs and benefits)
5. **How did it work out?** (Results and reflection)

### Example: Poor Technical Decision Description

❌ **Bad**:
> "We used React because it's popular and has a large ecosystem. It's a modern framework that works well for SPAs."

**Problems**:
- Generic (could apply to any project)
- No alternatives mentioned
- No specific context
- Buzzwords without substance
- No trade-offs acknowledged

### Example: Good Technical Decision Description

✅ **Good**:
> "We chose React over Vue or vanilla JavaScript for three reasons: First, the team had React experience, reducing onboarding time. Second, we needed a component library—Material UI offered 50+ pre-built components that would save 3-4 weeks of development. Third, the client wanted to eventually hire internally, and React's larger talent pool made that easier.
>
> The trade-off: React's larger bundle size (120KB vs Vue's 80KB) would slow initial load. We accepted this cost because most users (78% per analytics) were repeat visitors who'd benefit from caching, and the development speed gain was worth 200ms slower first load for new users."

**Why better**:
- Specific reasons tied to project context
- Alternatives explicitly considered
- Trade-offs acknowledged and justified
- Quantifiable details (bundle sizes, time saved, user stats)
- Shows thoughtful decision-making

---

## Explaining Technical Concepts

### Levels of Explanation

Adapt your explanation depth to the assumed audience:

**Level 1: Non-Technical** (Clients, recruiters, general audience)
Focus on: What it does, why it matters, what problem it solves

**Example**:
> "We implemented server-side rendering, which means pages load fully on the server before reaching users' browsers. This makes the site appear faster (users see content in 400ms instead of 2 seconds) and helps Google index it better, improving search rankings."

**Level 2: Technical Generalist** (Developers in different domains, mixed audience)
Focus on: How it works conceptually, key technologies, architectural patterns

**Example**:
> "We used Next.js for server-side rendering with React. Each page request generates HTML on the server, sends complete markup to the client, then hydrates it with JavaScript for interactivity. This improves Time to First Contentful Paint (TTFCP) from 2s to 400ms while maintaining the rich interactivity of a SPA."

**Level 3: Technical Specialist** (Hiring managers, senior engineers, technical deep-dives)
Focus on: Implementation details, code specifics, optimization techniques

**Example**:
> "We implemented getServerSideProps in Next.js for data-heavy pages, balancing server compute vs client wait time. For products with frequent inventory changes, SSR ensured price accuracy while ISR (Incremental Static Regeneration) handled slower-changing content like category pages. We set revalidation intervals to 60s based on inventory update frequency analysis, reducing API calls by 90% while keeping data fresh."

### The Layered Approach

Write for multiple audiences by layering complexity:

**Pattern**: Simple explanation → Technical detail → Code example

**Example**:
> **Simple**: "We optimized database queries to reduce page load time from 2 seconds to 200ms."
>
> **Technical**: "The bottleneck was N+1 queries—fetching user data, then looping to fetch each user's posts separately. We solved this with a LEFT JOIN, retrieving all data in a single query."
>
> **Code**:
> ```sql
> -- Before: 1 + N queries
> SELECT * FROM users WHERE id = 1;
> SELECT * FROM posts WHERE user_id = 1;  -- Repeated for each post
>
> -- After: 1 query
> SELECT users.*, posts.*
> FROM users
> LEFT JOIN posts ON users.id = posts.user_id
> WHERE users.id = 1;
> ```

---

## Code Snippets Best Practices

### When to Include Code

**Include code when**:
- It illustrates a key technical decision
- The implementation is clever or non-obvious
- It demonstrates your coding style
- It's short enough to read quickly (2-10 lines)

**Skip code when**:
- It's boilerplate or generic
- It requires too much context to understand
- It's longer than 15 lines
- Pseudocode or description would be clearer

### Code Snippet Structure

**Template**:
```
[Brief context explaining what this code does]

```language
// Before: [description of old approach]
[old code - optional]

// After: [description of new approach]
[new code]
```

[Explanation of why this matters or what it achieved]
```

**Example**:
```
Reducing bundle size was critical for mobile users. I replaced the heavyweight Moment.js library with native JavaScript Intl API:

```javascript
// Before: Moment.js (67KB gzipped)
import moment from 'moment';
const formatted = moment(date).format('MMMM D, YYYY');

// After: Native Intl (0KB - built into browsers)
const formatted = new Intl.DateTimeFormat('en-US', {
  year: 'numeric',
  month: 'long',
  day: 'numeric'
}).format(date);
```

This single change eliminated 67KB from our bundle, reducing load time by 400ms on 3G connections.
```

### Code Comments

Comments in case study code should:
- Explain the "why", not the "what"
- Highlight the key decision or technique
- Point out non-obvious trade-offs

❌ **Bad comments**:
```javascript
// Check if user exists
if (user) {
  // Do something
  doSomething();
}
```

✅ **Good comments**:
```javascript
// Optimistic UI: Update immediately, revert if server rejects
// This reduces perceived latency from 200ms to 0ms
updateUIImmediately(newValue);
try {
  await api.update(newValue);
} catch (error) {
  revertUI(oldValue);
  showErrorToast(error);
}
```

### Code Length Guidelines

**2-5 lines**: Perfect for case studies
- Shows technique without overwhelming
- Easy to read and understand
- Fits well in narrative flow

**6-10 lines**: Good if necessary
- Can show complete function or component
- May need before/after comparison
- Consider breaking into multiple snippets

**11-15 lines**: Use sparingly
- Only for critical, complex examples
- Must be genuinely interesting
- Consider linking to GitHub instead

**16+ lines**: Too long for case study
- Link to GitHub/Gist instead
- Or show just the critical excerpt

---

## Architecture and System Design

### Describing Architecture

**Pattern**: Overview → Components → Interactions → Rationale

**Example**:
> **Overview**: "I designed a three-tier architecture separating concerns clearly: React frontend, Node.js API layer, PostgreSQL database."
>
> **Components**: "The frontend handles presentation and user interaction. The API layer manages business logic, authentication, and data validation. PostgreSQL stores relational data with referential integrity."
>
> **Interactions**: "The frontend communicates with the API via REST endpoints. The API queries the database using Prisma ORM, which provides type-safe database access and automatic migrations."
>
> **Rationale**: "This separation allows independent scaling—we can scale the API horizontally without touching the database, and the frontend is served from a CDN. It also enables API reuse for future mobile apps."

### Architecture Diagrams

When describing architecture without visual diagrams, use ASCII art or clear text descriptions:

**ASCII Art Example**:
```
User Browser
     ↓
Cloudflare CDN (caching, DDoS protection)
     ↓
Load Balancer (AWS ALB)
     ↓
API Servers (3x t3.medium instances)
     ↓
PostgreSQL (RDS, primary + read replica)
     ↓
Redis Cache (ElastiCache)
```

**Text Description Example**:
> "The architecture follows a standard web application pattern:
> 1. Users access the React SPA served from Cloudflare's CDN
> 2. API requests route through AWS ALB to one of three Node.js servers
> 3. Each API server connects to PostgreSQL (read-heavy queries hit the replica)
> 4. Redis caches frequently-accessed data like user sessions and product catalogs
> 5. Background jobs run on separate workers to avoid blocking API responses"

---

## Balancing Jargon and Accessibility

### When to Use Technical Terms

**Use jargon when**:
- It's the standard industry term (REST API, not "web communication protocol")
- Explaining it would be longer and less clear
- Your audience is technical
- The term is searchable and well-documented

**Example using jargon correctly**:
> "I implemented JWT-based authentication with refresh tokens, storing access tokens in memory and refresh tokens in httpOnly cookies to prevent XSS attacks."

This assumes familiarity with JWTs, tokens, cookies, and XSS. Appropriate for technical audiences.

### When to Explain or Avoid Jargon

**Explain when**:
- The term is specialized or domain-specific
- It's critical to understanding your contribution
- Your audience is mixed (technical + non-technical)

**Example explaining jargon**:
> "I implemented JWT-based authentication—JSON Web Tokens that act like secure digital ID cards. Instead of checking credentials on every request (slow), the server issues a token after login that proves identity without database lookups, reducing auth latency by 95%."

### The "First Mention" Rule

**Rule**: Define terms on first use, even if technical

**Pattern**: `[Term] ([brief definition]) [usage]`

**Examples**:
- "We used GraphQL (a query language that lets clients request exactly the data they need) instead of REST."
- "I implemented debouncing (delaying function execution until user stops typing) to reduce API calls by 87%."
- "The app uses WebSockets (persistent two-way connections) for real-time updates, eliminating the need to poll the server."

After first definition, use the term normally.

---

## Writing About Performance

### Metrics That Matter

**Always include**:
- Baseline (before) numbers
- Optimized (after) numbers
- Improvement percentage or multiplier
- Context (what device, connection, conditions)

❌ **Vague**:
> "I made the app faster."

✅ **Specific**:
> "I reduced load time from 4.2 seconds to 800ms (81% improvement) on 3G connections by implementing code splitting and lazy loading images."

### Performance Vocabulary

**Prefer specific terms**:
- ✅ "Reduced Time to First Byte (TTFB)"
- ❌ "Made server faster"

- ✅ "Improved First Contentful Paint (FCP)"
- ❌ "Made page load faster"

- ✅ "Optimized Core Web Vitals (LCP, FID, CLS)"
- ❌ "Improved user experience"

### Performance Trade-offs

Always acknowledge what you sacrificed for performance:

**Example**:
> "Code splitting improved initial load time by 65% but introduced 50ms delays on route transitions. We accepted this trade-off because analytics showed 73% of users never navigated beyond the landing page—they needed fast first load more than fast subsequent navigation."

---

## Writing About Testing

### Testing Strategy Description

**Pattern**: What → How → Why → Coverage

**Example**:
> **What**: "I implemented a three-tier testing strategy: unit tests for business logic, integration tests for API endpoints, and end-to-end tests for critical user flows."
>
> **How**: "Unit tests used Jest and covered all utility functions and data transformations. Integration tests used Supertest to validate API contracts. E2E tests with Playwright covered authentication, checkout, and payment flows."
>
> **Why**: "This balance caught 94% of bugs before production while keeping CI time under 8 minutes. Pure unit tests would miss integration issues; pure E2E tests would be too slow and brittle."
>
> **Coverage**: "We maintained 85% code coverage and required all new features to include tests."

### Test Examples

If including test code, show one meaningful test:

**Example**:
```javascript
// This test caught a critical race condition in checkout
test('prevents duplicate orders from double-clicking submit', async () => {
  const submitButton = screen.getByRole('button', { name: /place order/i });

  // Simulate eager user double-clicking
  fireEvent.click(submitButton);
  fireEvent.click(submitButton);

  // Should only create one order
  await waitFor(() => {
    expect(createOrder).toHaveBeenCalledTimes(1);
  });
});
```

This shows: real-world scenario, clear intent, practical value

---

## Common Technical Writing Mistakes

### Mistake 1: Assuming Too Much Knowledge

❌ **Don't**:
> "I used Prisma's transaction API with the interactive pattern, leveraging $transaction to ensure atomicity across multiple model operations."

✅ **Do**:
> "I used Prisma's transaction system to ensure database operations either all succeed or all fail together (atomicity). For example, when processing a payment, both the charge and order creation must succeed—if either fails, both roll back to prevent inconsistent data."

### Mistake 2: Over-Explaining Simple Concepts

❌ **Don't**:
> "JavaScript is a programming language used for web development. React is a JavaScript library created by Facebook for building user interfaces using a component-based architecture where..."

✅ **Do**:
> "I chose React for its component reusability—building a design system once and reusing it across 50+ pages saved an estimated 200 development hours."

### Mistake 3: Listing Technologies Without Context

❌ **Don't**:
> "Tech stack: React, TypeScript, Node.js, Express, PostgreSQL, Redis, Docker, AWS, Terraform."

✅ **Do**:
> "Tech stack:
> - **React + TypeScript**: Type safety caught 40% of bugs at compile time
> - **Node.js + Express**: Familiar stack, easy deployment, good performance
> - **PostgreSQL**: Relational data with ACID guarantees for payment integrity
> - **Redis**: Session caching reduced database load by 70%
> - **Docker + AWS**: Consistent environments from dev to production"

### Mistake 4: Hiding Behind Buzzwords

❌ **Don't**:
> "Leveraged cutting-edge technologies to architect a robust, scalable, cloud-native solution using industry best practices and modern frameworks."

✅ **Do**:
> "Built a React SPA on AWS, scaling from 100 to 10,000 users with no architecture changes by choosing serverless (AWS Lambda + API Gateway) from day one. The trade-off: 100-200ms cold start latency, acceptable for our use case."

### Mistake 5: No Trade-offs Mentioned

Every technology choice has downsides. Acknowledging them shows maturity.

❌ **Don't**:
> "MongoDB was the perfect choice for this project."

✅ **Do**:
> "I chose MongoDB for flexible schemas during rapid prototyping, accepting the lack of foreign key constraints and eventual consistency of replica sets. Once the data model stabilized, we migrated to PostgreSQL for stronger guarantees."

---

## Technical Writing Checklist

Before finalizing technical content, verify:

**Clarity**:
- [ ] Technical terms defined on first use
- [ ] Jargon appropriate for target audience
- [ ] Complex concepts explained with examples or analogies

**Specificity**:
- [ ] Technologies named specifically (not "modern framework")
- [ ] Version numbers included when relevant
- [ ] Numbers and metrics quantify claims

**Depth**:
- [ ] Decisions include alternatives considered
- [ ] Rationale is clear and context-specific
- [ ] Trade-offs acknowledged honestly

**Code Quality**:
- [ ] Snippets are short (2-15 lines)
- [ ] Comments explain why, not what
- [ ] Code illuminates rather than obscures

**Architecture**:
- [ ] System components clearly described
- [ ] Interactions between components explained
- [ ] Scaling and performance considerations mentioned

**Credibility**:
- [ ] No buzzwords without substance
- [ ] Claims supported with evidence
- [ ] Tone confident but not arrogant
- [ ] Honest about limitations and challenges

---

## Examples: Before & After

### Example 1: Vague to Specific

❌ **Before**:
> "I built a modern web application using the latest technologies and best practices. The app is fast, secure, and scalable."

✅ **After**:
> "I built a React SPA using Next.js 14 for server-side rendering, reducing initial load time from 3.2s to 600ms. Authentication uses Auth0 (OAuth 2.0) to avoid rolling custom security. The app handles 5,000 concurrent users on a single AWS t3.medium instance, with horizontal scaling configured for traffic spikes."

### Example 2: Generic to Contextual

❌ **Before**:
> "We used microservices because they're scalable and follow best practices."

✅ **After**:
> "We used microservices for three services (auth, billing, notifications) but kept the core application as a monolith. This hybrid approach gave us isolation for critical services that needed independent scaling while avoiding the operational overhead of splitting everything. The monolith handles 90% of traffic; microservices handle the spiky 10%."

### Example 3: Buzzwords to Substance

❌ **Before**:
> "Leveraged cutting-edge AI/ML algorithms to deliver a paradigm-shifting, cloud-native solution."

✅ **After**:
> "Implemented collaborative filtering (user-based recommendations) to suggest products. The algorithm was simple—cosine similarity of purchase histories—but effective: 22% of users clicked recommendations, vs 3% baseline. Ran on a single Python FastAPI server, no need for TensorFlow or complex infrastructure."

---

## Voice and Tone Guidelines

### Confident, Not Arrogant

✅ **Confident**:
> "I identified the bottleneck in the data layer and optimized it, reducing query time from 2 seconds to 100ms."

❌ **Arrogant**:
> "I single-handedly saved the project by solving a problem no one else could figure out."

### Technical, Not Intimidating

✅ **Technical**:
> "I used PostgreSQL's partial indexes to speed up queries on soft-deleted records, reducing index size by 60% and improving query performance by 3x."

❌ **Intimidating**:
> "Obviously I used partial indexes, since any competent engineer would know that's the correct approach for this scenario."

### Honest, Not Self-Deprecating

✅ **Honest**:
> "My first approach—caching everything—made things worse. I learned to profile before optimizing and fixed the actual bottleneck: N+1 queries."

❌ **Self-deprecating**:
> "I have no idea what I'm doing and got lucky when this somehow worked."

---

## Final Thought: Write Like You're Teaching

The best technical writing teaches something:

- **Hire managers learn** how you think and solve problems
- **Clients learn** the value you delivered
- **Fellow developers learn** techniques they can apply

If your reader learns nothing, rewrite until they do.
