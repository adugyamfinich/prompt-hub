# Prompt Evaluation Guide

How to test and measure the effectiveness of your prompts.

## Why Evaluate Prompts?

Effective prompts are:
- **Reliable** - Produce consistent results
- **Accurate** - Give correct/useful outputs
- **Efficient** - Get good results without excessive iteration
- **Clear** - Easy for users to understand and customize

## Evaluation Framework

### 1. Define Success Criteria

Before testing, establish what "success" means for your prompt.

**Example criteria:**
```
✅ Produces output in correct format 100% of time
✅ Identifies at least 90% of relevant issues
✅ Explanation is comprehensible to beginners
✅ Works across 3+ different test cases
✅ Completes task in single interaction
```

### 2. Create Test Cases

Develop diverse test inputs:

**Good test set includes:**
- ✅ Typical use case (happy path)
- ✅ Edge cases (unusual but valid)
- ✅ Boundary conditions (limits)
- ✅ Error conditions (invalid input)
- ✅ Ambiguous cases (unclear intent)

**Example for code debugging prompt:**
```
Test 1: Simple syntax error (typical)
Test 2: Logical error with no exception (edge case)
Test 3: Empty function (boundary)
Test 4: Malformed code (error condition)
Test 5: Code with multiple possible issues (ambiguous)
```

### 3. Run Tests

Execute your prompt with each test case and document:
- Input provided
- Output received
- Whether it met success criteria
- Any unexpected behaviors
- Time/tokens used

### 4. Analyze Results

Calculate metrics:
- **Success rate**: % of tests that met criteria
- **Consistency**: Variation across multiple runs
- **Efficiency**: Average tokens or time needed
- **Robustness**: Performance on edge cases

## Evaluation Metrics

### Accuracy

**How to measure:**
- Compare output to expected result
- Have domain experts review quality
- Test against known correct answers

**For subjective tasks:**
- Use rating scale (1-5)
- Multiple evaluators
- Inter-rater reliability

### Consistency

**Test by:**
- Running same input multiple times
- Checking for variation in outputs
- Measuring similarity between runs

**Good consistency:**
- Deterministic tasks: Identical outputs
- Creative tasks: Same quality/structure, varied details

### Completeness

**Check if output includes:**
- All required elements
- Proper format/structure
- Necessary context/explanations

**Scoring:**
```
5/5 - All elements present and well-formed
4/5 - Minor omissions or formatting issues
3/5 - Missing some required elements
2/5 - Incomplete or poorly structured
1/5 - Major elements missing
```

### Efficiency

**Measure:**
- Tokens used (shorter is better)
- Number of interactions needed
- Time to completion

**Calculate cost:**
```
Cost per use = (prompt tokens + output tokens) × price per token
```

### Robustness

**Test across:**
- Different input lengths
- Various formats
- Multiple domains
- Different AI models

**Robustness score:**
```
(Successful test cases / Total test cases) × 100
```

## Testing Methodology

### A/B Testing

Compare two prompt versions:

```
Prompt A: "Explain this code"
Prompt B: "Explain this code line by line, including purpose and potential issues"

Test with 10 code samples
Measure: clarity rating, completeness, user satisfaction
Winner: Prompt with higher average scores
```

### Regression Testing

When updating a prompt:
1. Save outputs from current version
2. Run same inputs through new version
3. Compare results
4. Ensure improvements don't break existing functionality

### Cross-Model Testing

Test prompt on multiple AI models:
```
Test on:
- Claude Sonnet
- GPT-4
- Gemini Pro

Compare:
- Output quality
- Consistency
- Format compliance
```

Document which models work best.

### User Testing

Real users are the ultimate test:
1. Provide prompt to target users
2. Collect feedback on:
   - Ease of use
   - Output quality
   - Areas of confusion
3. Iterate based on findings

## Evaluation Checklist

Before submitting a prompt, verify:

### Functionality
- [ ] Produces expected output type
- [ ] Handles typical inputs correctly
- [ ] Manages edge cases gracefully
- [ ] Fails safely on invalid input
- [ ] Provides useful error guidance

### Quality
- [ ] Output is accurate/useful
- [ ] Explanations are clear
- [ ] Format is consistent
- [ ] Level of detail is appropriate
- [ ] Tone matches intent

### Usability
- [ ] Instructions are clear
- [ ] Variables are well-documented
- [ ] Examples are representative
- [ ] Limitations are stated
- [ ] Easy to customize

### Reliability
- [ ] Consistent across runs
- [ ] Works on stated models
- [ ] Handles variations gracefully
- [ ] Produces similar quality output
- [ ] No unexpected failures

### Efficiency
- [ ] Completes task in reasonable time
- [ ] Doesn't use excessive tokens
- [ ] Avoids unnecessary steps
- [ ] Gets to the point quickly

## Common Issues and Solutions

### Issue: Inconsistent Outputs

**Diagnosis:**
- Prompt is too open-ended
- Missing constraints
- Ambiguous instructions

**Solutions:**
- Add specific requirements
- Include output format specification
- Provide more examples
- Use structured output format

### Issue: Too Verbose

**Diagnosis:**
- Prompt asks for too much detail
- No length constraints
- Instructions encourage elaboration

**Solutions:**
- Specify desired length
- Ask for "concise" or "brief" output
- Limit number of items/points
- Use "summarize" language

### Issue: Missing Key Information

**Diagnosis:**
- Incomplete task specification
- Unclear priorities
- Insufficient context

**Solutions:**
- List all required elements explicitly
- Prioritize what's most important
- Add relevant background
- Include "must include" section

### Issue: Format Not Followed

**Diagnosis:**
- Format specification unclear
- Examples don't match specification
- Too flexible in instructions

**Solutions:**
- Show exact format with placeholders
- Make format requirements explicit
- Use structured output (JSON, XML)
- Add "strictly follow this format" instruction

### Issue: Model-Specific Failures

**Diagnosis:**
- Uses model-specific features
- Assumptions about capabilities
- Format preferences differ

**Solutions:**
- Test on all target models
- Document model differences
- Create model-specific versions
- Use universal techniques

## Documentation Standards

Record evaluation results in prompt file:

```markdown
## Performance Notes

### Testing Methodology
Tested on: Claude Sonnet 4, GPT-4
Test cases: 15 diverse inputs
Date: 2024-01-15

### Results
- Success rate: 93% (14/15 passed)
- Average quality score: 4.2/5
- Consistency: High (97% similarity across runs)
- Failed case: Extremely large input (5000+ lines)

### Strengths
- Excellent at identifying logic errors
- Clear explanations
- Consistent formatting
- Works well with Python, JavaScript, Java

### Limitations
- Struggles with very large codebases (>1000 lines)
- Less effective with esoteric languages
- May miss subtle performance issues
- Explanations assume intermediate knowledge

### Tips for Best Results
- Break large files into smaller functions
- Provide context about what code should do
- Mention your experience level
- Include error messages if available
```

## Continuous Improvement

### Monitoring

Track over time:
- User feedback/ratings
- Issue reports
- Success stories
- Common modifications users make

### Iteration Cycle

```
1. Collect feedback
2. Identify patterns
3. Propose improvements
4. Test changes
5. Document updates
6. Release new version
```

### Version Control

Keep old versions for comparison:
- Document what changed
- Why it changed
- Impact on performance
- Migration guide if needed

## Automated Testing (Advanced)

For power users, automate evaluation:

```python
# Example test script
def test_prompt(prompt_template, test_cases):
    results = []
    for test in test_cases:
        # Substitute variables
        prompt = prompt_template.format(**test['input'])
        
        # Run through AI model
        output = ai_model.generate(prompt)
        
        # Evaluate
        score = evaluate_output(
            output, 
            test['expected'],
            test['criteria']
        )
        
        results.append({
            'test': test['name'],
            'score': score,
            'output': output
        })
    
    return generate_report(results)
```

## Evaluation Resources

### Tools
- **LangSmith**: Track prompt performance
- **PromptFoo**: Automated prompt testing
- **Weights & Biases**: Log experiments
- **Custom scripts**: Build your own evaluator

### Metrics Libraries
- BLEU score (translation quality)
- ROUGE score (summarization quality)
- BERTScore (semantic similarity)
- Human evaluation templates

### Community Feedback

Leverage the PromptHub community:
- Star ratings via GitHub reactions
- Issue reports for problems
- Discussion threads for improvements
- Success stories in comments

## Publishing Evaluation Results

When submitting a prompt, include:

1. **Test methodology** - How you evaluated
2. **Sample size** - Number of tests run
3. **Success rate** - % that met criteria
4. **Model coverage** - Which models tested
5. **Limitations found** - Known issues
6. **Best practices** - Tips from testing

This helps users understand reliability and appropriate use cases.

---

**[Back to Main README](../README.md)** | **[Best Practices](best-practices.md)** | **[Taxonomy Guide](taxonomy.md)**
