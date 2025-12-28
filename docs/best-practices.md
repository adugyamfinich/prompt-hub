# Best Practices for AI Prompts

This guide provides proven techniques for crafting effective AI prompts based on research and community experience.

## Table of Contents

- [Core Principles](#core-principles)
- [Prompt Structure](#prompt-structure)
- [Techniques](#techniques)
- [Common Pitfalls](#common-pitfalls)
- [Model-Specific Tips](#model-specific-tips)
- [Testing and Iteration](#testing-and-iteration)

## Core Principles

### 1. Be Clear and Specific

❌ **Bad:** "Help me with code"
✅ **Good:** "Debug this Python function that should sort a list but is returning None"

- State exactly what you want
- Provide context and constraints
- Define success criteria

### 2. Provide Context

The more relevant context you provide, the better the output:

```
You are a [ROLE] with expertise in [DOMAIN].

Context: [BACKGROUND INFORMATION]
Task: [WHAT TO DO]
Constraints: [LIMITATIONS OR REQUIREMENTS]
Output: [DESIRED FORMAT]
```

### 3. Use Examples

Show, don't just tell:

```
Convert these items to the specified format:

Input: "apple, banana, cherry"
Output: ["apple", "banana", "cherry"]

Input: "dog, cat, bird"
Output: [YOUR EXPECTED OUTPUT]

Now convert: "red, blue, green"
```

### 4. Break Down Complex Tasks

Instead of one massive prompt, use step-by-step instructions:

```
Follow these steps:
1. Analyze the input data for patterns
2. Identify any anomalies or outliers
3. Suggest corrections for each issue
4. Provide a summary of changes
```

## Prompt Structure

### Basic Template

```
[ROLE DEFINITION]
You are an expert [ROLE] specializing in [DOMAIN].

[CONTEXT]
Background: [RELEVANT INFORMATION]

[TASK]
Your task is to [PRIMARY OBJECTIVE].

[REQUIREMENTS]
- Requirement 1
- Requirement 2
- Requirement 3

[CONSTRAINTS]
- Do not include [UNWANTED ELEMENTS]
- Limit response to [SCOPE]

[OUTPUT FORMAT]
Provide your response as [DESIRED FORMAT].
```

### Advanced Structure with Chain-of-Thought

```
You are [ROLE].

OBJECTIVE: [MAIN GOAL]

PROCESS:
1. First, [STEP 1]
2. Then, [STEP 2]
3. Next, [STEP 3]
4. Finally, [STEP 4]

For each step, explain your reasoning before providing the result.

INPUT: [YOUR INPUT]

Begin your analysis.
```

## Techniques

### Chain-of-Thought (CoT)

Encourage step-by-step reasoning:

```
Let's solve this step by step:
1. What do we know?
2. What do we need to find?
3. What's our approach?
4. Execute the approach
5. Verify the result
```

**When to use:** Complex problems, mathematical reasoning, debugging, analysis

### Few-Shot Learning

Provide multiple examples:

```
Convert these sentences to past tense:

Present: "I walk to the store"
Past: "I walked to the store"

Present: "She eats breakfast"
Past: "She ate breakfast"

Present: "They swim in the pool"
Past: [YOUR TURN]
```

**When to use:** Pattern recognition, formatting tasks, style transfer

### Role-Playing

Assign a specific persona:

```
You are a senior Python developer with 10 years of experience 
reviewing code for production systems. You prioritize:
- Security
- Performance
- Maintainability
- Best practices

Review this code with these priorities in mind: [CODE]
```

**When to use:** Domain expertise needed, specific perspective required

### Structured Output

Request specific formats:

```
Analyze this text and return a JSON object with:
{
  "sentiment": "positive|negative|neutral",
  "key_topics": ["topic1", "topic2"],
  "summary": "brief summary",
  "confidence": 0.0-1.0
}

Text: [YOUR TEXT]
```

**When to use:** Parsing, data extraction, API responses

### Iterative Refinement

Build in revision cycles:

```
Create a product description for [PRODUCT].

After creating it, review it for:
- Clarity
- Persuasiveness
- Accuracy
- SEO keywords

Then provide a revised version incorporating improvements.
```

**When to use:** Creative content, writing, design critiques

## Common Pitfalls

### ❌ Being Too Vague

**Problem:** "Make this better"
**Solution:** "Improve this code's readability by adding comments and using descriptive variable names"

### ❌ Assuming Knowledge

**Problem:** "Fix the bug" (without providing the code)
**Solution:** Always provide necessary context and materials

### ❌ Conflicting Instructions

**Problem:** "Be concise but provide detailed explanations"
**Solution:** Prioritize clearly: "Provide a brief summary followed by detailed explanations"

### ❌ Forgetting Edge Cases

**Problem:** Not mentioning how to handle empty inputs, errors, etc.
**Solution:** Explicitly state: "If the input is empty, return null"

### ❌ Overcomplicating

**Problem:** 500-word prompt for a simple task
**Solution:** Keep it simple when appropriate

## Model-Specific Tips

### Claude
- Excels at long-form content and analysis
- Responds well to ethical guidelines
- Good at refusing inappropriate requests
- Strong with structured reasoning

**Tip:** Use XML-style tags for complex structures:
```
<context>
Your context here
</context>

<task>
Your task here
</task>
```

### GPT (OpenAI)
- Strong creative capabilities
- Good with code generation
- Responds well to system messages
- Effective with temperature settings

**Tip:** Use system messages for persistent instructions

### Gemini (Google)
- Excellent multimodal capabilities
- Strong at factual queries
- Good at following complex instructions
- Effective with structured data

**Tip:** Leverage multimodal inputs when available

## Testing and Iteration

### 1. Test with Edge Cases

Try your prompt with:
- Empty inputs
- Very long inputs
- Unusual formatting
- Ambiguous cases

### 2. Iterate Based on Results

```
Version 1: "Summarize this article"
→ Too vague, inconsistent length

Version 2: "Summarize this article in 3-5 sentences"
→ Better, but missing key points

Version 3: "Summarize this article in 3-5 sentences, 
focusing on the main argument and supporting evidence"
→ Good results!
```

### 3. A/B Test Variations

Compare different approaches:
- Formal vs. conversational tone
- With/without examples
- Different role definitions
- Various output formats

### 4. Document What Works

Keep a record of successful prompts and patterns for future use.

## Prompt Optimization Checklist

Before finalizing a prompt, check:

- [ ] Clear objective stated
- [ ] Necessary context provided
- [ ] Specific requirements listed
- [ ] Output format defined
- [ ] Examples included (if helpful)
- [ ] Edge cases addressed
- [ ] Constraints specified
- [ ] Role/expertise defined (if needed)
- [ ] Tested with sample inputs
- [ ] Produces consistent results

## Advanced Techniques

### Prompt Chaining

Break complex tasks into sequential prompts:

```
Prompt 1: "Extract all dates from this document"
→ Get list of dates

Prompt 2: "Convert these dates to ISO format: [DATES]"
→ Get formatted dates

Prompt 3: "Create a timeline from these events: [FORMATTED_DATES]"
→ Get final timeline
```

### Self-Consistency

Ask for multiple attempts and combine:

```
Solve this problem 3 different ways, then identify 
which solution is most accurate and why.
```

### Meta-Prompting

Ask the AI to help improve your prompt:

```
I'm trying to create a prompt that [OBJECTIVE].
My current prompt is: [YOUR PROMPT]
How can I improve it for better results?
```

## Resources

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Prompt Engineering Guide by DAIR.AI](https://www.promptingguide.ai/)

## Contributing

Found a technique that works well? Submit it as a new prompt to PromptHub!

---

**[Back to Main README](../README.md)**
