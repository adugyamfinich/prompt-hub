# PromptHub Taxonomy Guide

This guide explains how we organize and categorize prompts in PromptHub.

## Organization Structure

PromptHub uses a three-dimensional categorization system:

1. **By Category** - What domain or use case
2. **By Model** - Which AI model(s) it's optimized for
3. **By Technique** - What prompting method it uses

This allows users to find prompts multiple ways depending on their needs.

## Primary Categories

### 🖥️ Coding

**Definition:** Prompts related to software development, programming, and technical tasks.

**Subcategories:**
- **Code Generation**: Creating new code from specifications
- **Debugging**: Finding and fixing errors
- **Code Review**: Analyzing code quality and best practices
- **Refactoring**: Improving existing code structure
- **Documentation**: Generating comments and docs
- **Testing**: Creating unit tests and test cases
- **Algorithm Design**: Solving computational problems

**Examples:**
- "Debug my Python function that's throwing a TypeError"
- "Generate unit tests for this React component"
- "Review this code for security vulnerabilities"

**When to use this category:** Any prompt primarily focused on code or software development.

---

### ✍️ Writing

**Definition:** Prompts for creating, editing, or improving written content.

**Subcategories:**
- **Creative Writing**: Stories, poems, scripts
- **Business Writing**: Emails, reports, proposals
- **Technical Writing**: Manuals, specifications, how-tos
- **Marketing Copy**: Ads, landing pages, slogans
- **Academic Writing**: Essays, papers, thesis
- **Editing**: Proofreading, grammar, style improvement
- **Translation**: Converting between languages

**Examples:**
- "Write a professional email declining a meeting"
- "Create a short story about time travel"
- "Improve this paragraph for clarity and impact"

**When to use this category:** When the primary goal is text production or improvement.

---

### 📊 Analysis

**Definition:** Prompts for interpreting, analyzing, or deriving insights from information.

**Subcategories:**
- **Data Analysis**: Interpreting datasets and statistics
- **Text Analysis**: Sentiment, themes, patterns in text
- **Comparison**: Evaluating options or alternatives
- **Summarization**: Condensing information
- **Trend Analysis**: Identifying patterns over time
- **Decision Support**: Evaluating choices with criteria
- **Root Cause Analysis**: Finding underlying issues

**Examples:**
- "Analyze customer feedback for common themes"
- "Compare these three investment options"
- "Summarize this 50-page report into key takeaways"

**When to use this category:** When the primary task involves understanding or interpreting information.

---

### 🎨 Creative

**Definition:** Prompts for artistic, imaginative, or innovative content creation.

**Subcategories:**
- **Storytelling**: Narrative development
- **Brainstorming**: Idea generation
- **Character Development**: Creating personas
- **World Building**: Designing settings and lore
- **Art Direction**: Visual concept development
- **Naming**: Product names, brand names, character names
- **Game Design**: Mechanics, puzzles, quests

**Examples:**
- "Generate 10 innovative startup ideas in healthcare"
- "Create a fantasy world with unique magic system"
- "Develop a complex antagonist character"

**When to use this category:** When creativity and imagination are the primary focus.

---

### 📚 Education

**Definition:** Prompts for teaching, learning, explaining, or training.

**Subcategories:**
- **Lesson Planning**: Curriculum development
- **Explanation**: Breaking down complex topics
- **Quiz Creation**: Generating assessments
- **Study Guides**: Learning materials
- **Tutoring**: Personalized instruction
- **Simplification**: Making content accessible
- **Concept Mapping**: Visualizing relationships

**Examples:**
- "Explain quantum physics to a 10-year-old"
- "Create a lesson plan for teaching Python loops"
- "Generate practice problems for calculus"

**When to use this category:** When the goal is learning or knowledge transfer.

---

### 🔬 Research

**Definition:** Prompts for scholarly investigation, literature review, or academic inquiry.

**Subcategories:**
- **Literature Review**: Summarizing existing research
- **Hypothesis Generation**: Formulating testable ideas
- **Methodology Design**: Planning research approaches
- **Data Collection**: Survey and interview design
- **Citation Management**: Formatting references
- **Research Questions**: Identifying knowledge gaps
- **Systematic Review**: Comprehensive analysis

**Examples:**
- "Design a research methodology for studying social media impact"
- "Generate research questions about climate change"
- "Summarize key findings from these papers"

**When to use this category:** When conducting or supporting academic/scientific research.

## Model-Specific Organization

### Why Model-Specific Prompts?

Different AI models have unique strengths and respond differently to prompting techniques. Some prompts are optimized for specific models.

### Model Categories

#### Claude (Anthropic)
**Characteristics:**
- Excellent at long-form content
- Strong reasoning capabilities
- Good at following complex instructions
- Responds well to XML-style tags
- Tends to be more conservative with certain content

**Best for:**
- Detailed analysis
- Ethical decision-making
- Technical documentation
- Structured reasoning tasks

#### GPT (OpenAI)
**Characteristics:**
- Strong creative capabilities
- Good at code generation
- Responds well to system messages
- More experimental with creative content
- Excellent at pattern completion

**Best for:**
- Creative writing
- Code generation
- Conversational tasks
- Brainstorming

#### Gemini (Google)
**Characteristics:**
- Excellent multimodal capabilities
- Strong at factual queries
- Good with structured data
- Effective with real-world information

**Best for:**
- Multimodal tasks (text + image)
- Factual queries
- Structured data processing

### Cross-Model Compatibility

Most prompts work across models with minor adjustments. Look for:
- **"All Models"** - Works well everywhere
- **"Claude, GPT"** - Optimized for these but adaptable
- **"Claude Only"** - Uses Claude-specific features

## Technique-Based Organization

### Chain-of-Thought (CoT)

**Definition:** Prompts that encourage step-by-step reasoning.

**Structure:**
```
1. Understand the problem
2. Break into sub-problems
3. Solve each part
4. Combine solutions
5. Verify result
```

**When to use:**
- Complex problems
- Mathematical reasoning
- Logical deduction
- Debugging

**Example prompts:**
- Mathematical problem solvers
- Code debuggers with explanation
- Logical reasoning tasks

---

### Few-Shot Learning

**Definition:** Prompts that provide multiple examples to establish a pattern.

**Structure:**
```
Example 1: Input → Output
Example 2: Input → Output
Example 3: Input → Output

Now process: [Your Input]
```

**When to use:**
- Pattern recognition tasks
- Format conversion
- Style mimicking
- Classification

**Example prompts:**
- Data format converters
- Style transfer for writing
- Classification tasks

---

### Role-Playing

**Definition:** Prompts that assign a specific persona or expertise to the AI.

**Structure:**
```
You are a [ROLE] with [EXPERIENCE] in [DOMAIN].
Your approach is characterized by [TRAITS].

Task: [WHAT TO DO]
```

**When to use:**
- Need domain expertise
- Want specific perspective
- Require consistent personality
- Task-specific optimization

**Example prompts:**
- Technical code reviewer
- Senior consultant
- Historical expert
- Career counselor

---

### Structured Output

**Definition:** Prompts that request specific output formats (JSON, tables, etc.).

**Structure:**
```
Analyze X and return in this format:
{
  "field1": "value",
  "field2": ["item1", "item2"],
  "field3": {nested}
}
```

**When to use:**
- API integration
- Data extraction
- Parsing tasks
- Automated processing

**Example prompts:**
- JSON data extractors
- Table generators
- Form fillers
- Structured analyzers

## Metadata Standards

Each prompt must include complete metadata:

### Required Fields

```markdown
- **Category**: [One of: Coding, Writing, Analysis, Creative, Education, Research]
- **Difficulty**: [Beginner | Intermediate | Advanced]
- **Model Compatibility**: [Claude, GPT-4, Gemini, All Models]
- **Tags**: `#tag1` `#tag2` `#tag3`
- **Author**: @github-username
- **Date Added**: YYYY-MM-DD
- **Version**: X.Y
```

### Tagging Guidelines

**Good tags are:**
- Specific: `#python` not `#programming`
- Searchable: Common terms people would use
- Relevant: Directly related to prompt's purpose
- Concise: 1-2 words each

**Tag categories:**
- **Language/Tech**: `#python`, `#javascript`, `#react`
- **Domain**: `#healthcare`, `#finance`, `#education`
- **Task**: `#debugging`, `#optimization`, `#summarization`
- **Format**: `#json`, `#markdown`, `#table`
- **Level**: `#beginner`, `#advanced`

**Avoid:**
- Generic tags: `#ai`, `#help`, `#useful`
- Redundant tags: Don't repeat the category
- Too many tags: 5-7 maximum

## Difficulty Ratings

### 🟢 Beginner

**Characteristics:**
- Straightforward task
- Minimal customization needed
- Clear, simple structure
- Works reliably out-of-the-box
- Requires no AI expertise

**Examples:**
- "Summarize this text in 3 sentences"
- "Fix grammar errors"
- "Generate 5 name ideas"

**User expectation:** Copy, fill in variables, use.

---

### 🟡 Intermediate

**Characteristics:**
- May require some customization
- Multiple variables to configure
- Benefits from understanding context
- May need iteration for best results
- Assumes basic prompting knowledge

**Examples:**
- "Debug code with explanation"
- "Analyze data and provide insights"
- "Generate content in specific style"

**User expectation:** Understand the prompt structure, adjust as needed.

---

### 🔴 Advanced

**Characteristics:**
- Complex multi-step process
- Requires domain knowledge
- Extensive customization needed
- May involve prompt chaining
- Assumes expert prompting skills

**Examples:**
- "Multi-stage research workflow"
- "Complex data pipeline analysis"
- "Advanced algorithmic problem solving"

**User expectation:** Deep understanding of task and prompting techniques.

## Filing Guidelines

### Where to Place a Prompt

A prompt can exist in multiple locations:

1. **Primary location**: `prompts/by-category/[category]/`
2. **Model-specific copy** (if optimized): `prompts/by-model/[model]/`
3. **Technique-based copy** (if it's a good example): `prompts/by-technique/[technique]/`

### Naming Conventions

**File names:**
- Use kebab-case: `my-prompt-name.md`
- Be descriptive: `python-debugger-with-explanations.md` not `debugger.md`
- Keep under 50 characters
- No version numbers in filename

**Prompt titles:**
- Use Title Case: "Python Code Debugger Pro"
- Be specific and searchable
- Include key terms users would search for
- Avoid generic names: "Helper", "Assistant", "Tool"

## Evolution and Updates

### When to Update a Prompt

- User reports issues
- Better approach discovered
- Model capabilities change
- New use cases emerge

### Versioning

Follow semantic versioning:
- **Major (X.0)**: Breaking changes, complete rewrite
- **Minor (X.Y)**: New features, improvements, expanded scope
- **Note**: We only use major.minor, no patch versions

### Deprecation

If a prompt becomes obsolete:
1. Add `[DEPRECATED]` to title
2. Explain why in description
3. Link to replacement
4. Keep for historical reference

## Quality Criteria

All prompts must:
- ✅ Have a clear, specific purpose
- ✅ Include working examples
- ✅ Document limitations honestly
- ✅ Be reproducible across uses
- ✅ Follow template format
- ✅ Have complete metadata
- ✅ Pass validation script

## Contributing to Taxonomy

Think a category is missing or taxonomy should change?

1. Open a [Discussion](https://github.com/adugyamfinich/prompt-hub/discussions)
2. Explain the problem with current system
3. Propose a solution with examples
4. Get community feedback
5. If approved, submit a PR updating this guide

---

**[Back to Main README](../README.md)** | **[Contributing Guide](../CONTRIBUTING.md)** | **[Best Practices](best-practices.md)**
