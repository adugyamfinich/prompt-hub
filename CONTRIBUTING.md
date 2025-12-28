# Contributing to PromptHub

Thank you for your interest in contributing to PromptHub! This guide will help you submit high-quality prompts that benefit the entire community.

## 🎯 How to Contribute

### Option 1: Submit via Pull Request (Recommended)

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/prompt-hub.git
   cd prompt-hub
   ```

3. **Create a new branch**
   ```bash
   git checkout -b add-prompt-[prompt-name]
   ```

4. **Add your prompt**
   - Copy `templates/prompt-template.md`
   - Fill in all required sections
   - Place in appropriate category folder
   - Name file using kebab-case: `your-prompt-name.md`

5. **Validate your prompt**
   ```bash
   python scripts/validate_prompt.py prompts/by-category/[category]/your-prompt-name.md
   ```

6. **Commit and push**
   ```bash
   git add .
   git commit -m "Add: [Your Prompt Name]"
   git push origin add-prompt-[prompt-name]
   ```

7. **Create a Pull Request**
   - Use the PR template
   - Link any related issues
   - Wait for review (usually 2-3 days)

### Option 2: Submit via Issue

If you're not comfortable with Git:
1. Go to [Issues](../../issues)
2. Click "New Issue"
3. Select "Prompt Submission"
4. Fill out the template
5. A maintainer will create the PR for you

## ✅ Quality Guidelines

### Required Elements

Every prompt must include:
- [ ] **Clear Description** - What does this prompt do?
- [ ] **Use Case** - When should someone use it?
- [ ] **The Prompt** - The actual prompt text
- [ ] **Variables** - Any customizable elements
- [ ] **Example Input/Output** - At least one working example
- [ ] **Metadata** - Category, difficulty, model compatibility
- [ ] **Performance Notes** - Strengths and limitations

### Quality Standards

✅ **Good Prompt Submissions:**
- Clear and specific purpose
- Reproducible across multiple runs
- Well-tested on stated models
- Includes context for customization
- Documents limitations honestly
- Provides meaningful examples

❌ **Avoid:**
- Vague or overly general prompts
- Untested prompts
- Prompts that produce harmful content
- Duplicate submissions (search first!)
- Prompts without examples
- Missing metadata

## 📝 Prompt Template Usage

Use the template at `templates/prompt-template.md`. Here's what each section should contain:

### Metadata
```markdown
- **Category**: Choose ONE: Coding, Writing, Analysis, Creative, Education, Research
- **Difficulty**: Beginner, Intermediate, or Advanced
- **Model Compatibility**: Which AI models work well (test at least one)
- **Tags**: Relevant keywords for searchability
- **Author**: Your GitHub username
- **Date Added**: Submission date
- **Version**: Start with 1.0
```

### Description
2-3 sentences explaining what the prompt does and its primary value.

### Use Case
Specific scenarios where this prompt excels. Be concrete!

### The Prompt
The actual prompt text. Use `{VARIABLES}` in curly braces for customizable parts.

### Variables to Customize
List each variable with a clear explanation of what users should input.

### Example Input/Output
Show the prompt in action. Include:
- The customized prompt (variables filled in)
- The actual output received
- Any notes on variations

### Performance Notes
- **Strengths**: What it does exceptionally well
- **Limitations**: Known weaknesses or edge cases
- **Tips**: How to get the best results

## 🏷️ Categorization

### Primary Categories
- **Coding**: Programming, debugging, code review, documentation
- **Writing**: Articles, emails, creative writing, editing
- **Analysis**: Data interpretation, research, summarization
- **Creative**: Art, storytelling, brainstorming, design
- **Education**: Teaching, explaining, learning assistance
- **Research**: Literature review, hypothesis generation, methodology

### Techniques
- **Chain-of-thought**: Step-by-step reasoning prompts
- **Few-shot**: Prompts with multiple examples
- **Role-playing**: Persona-based prompts
- **Structured-output**: Prompts for specific formats (JSON, tables, etc.)

### Model-Specific
Place a copy in the model folder if the prompt is optimized for or only works with specific models.

## 🔍 Review Process

### What Reviewers Check
1. **Format Compliance** - Follows template structure
2. **Completeness** - All required sections filled
3. **Quality** - Clear, useful, well-documented
4. **Testing** - Examples are reproducible
5. **Uniqueness** - Not a duplicate
6. **Safety** - No harmful content

### Timeline
- **Initial Review**: Within 3 days
- **Feedback**: Reviewer may request changes
- **Approval**: Requires 2 approvals from maintainers
- **Merge**: Usually within 1 week of submission

## 🚫 Content Guidelines

### Prohibited Content
We do **NOT** accept prompts that:
- Generate harmful, hateful, or discriminatory content
- Assist in illegal activities
- Violate privacy or impersonate individuals
- Produce misleading information intentionally
- Exploit vulnerabilities or create malware
- Generate NSFW content without clear warnings and purpose

### Gray Areas
If your prompt touches on sensitive topics:
- Include clear warnings in the description
- Explain the legitimate use case
- Document safety considerations
- Be prepared for extra scrutiny

## 🎨 Naming Conventions

### File Names
- Use kebab-case: `my-prompt-name.md`
- Be descriptive but concise
- Match the prompt's primary function

### Prompt Titles
- Use Title Case: "Code Debugger Pro"
- Be specific and searchable
- Avoid generic names like "Helper" or "Assistant"

## 🐛 Reporting Issues

Found a problem with an existing prompt?

1. Check if an issue already exists
2. Open a new issue with:
   - Prompt name and location
   - What's wrong or could be improved
   - Example of the problem (if applicable)
   - Suggested fix (optional)

## 💡 Suggesting Improvements

Have an idea to make PromptHub better?
- Open a discussion in [Discussions](../../discussions)
- Tag it appropriately (enhancement, documentation, etc.)
- Explain the problem and your proposed solution

## 🏅 Recognition

Contributors are recognized in:
- Monthly contributor highlights
- README top contributors section
- Release notes
- Prompt authorship metadata

## 📞 Getting Help

- **Questions**: Use [Discussions](../../discussions)
- **Bug Reports**: Use [Issues](../../issues)
- **Real-time Help**: Check if we have a Discord/Slack (TBD)

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License. Individual prompts may include additional attribution requirements.

---

**Thank you for helping build the world's best prompt library! 🚀**
