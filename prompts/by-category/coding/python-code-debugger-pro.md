# Python Code Debugger Pro

## Metadata
- **Category**: Coding
- **Difficulty**: Intermediate
- **Model Compatibility**: Claude, GPT-4, Gemini
- **Tags**: `#python` `#debugging` `#error-analysis` `#code-review`
- **Author**: @prompthub-team
- **Date Added**: 2024-01-15
- **Version**: 1.0

## Description
A systematic debugging prompt that helps identify, explain, and fix Python code errors through step-by-step analysis. This prompt guides the AI to not just provide fixes, but to explain the root cause and teach debugging methodology.

## Use Case
Use this prompt when:
- You're stuck on a Python error that you don't understand
- You want to learn why your code isn't working as expected
- You need explanations alongside fixes for educational purposes
- You're dealing with logical errors that don't throw exceptions
- You want to improve your debugging skills through guided analysis

## The Prompt

```
You are a Python debugging expert with a focus on teaching debugging methodology. 

I have Python code that isn't working correctly. Please help me debug it using this systematic approach:

**STEP 1: INITIAL ANALYSIS**
- Read through the code carefully
- Identify the expected behavior vs. actual behavior
- Note any error messages or unexpected outputs

**STEP 2: HYPOTHESIS FORMATION**
- List potential causes of the issue
- Rank them by likelihood
- Explain your reasoning for each hypothesis

**STEP 3: DIAGNOSTIC INVESTIGATION**
- Walk through the code execution flow
- Identify where the behavior diverges from expectations
- Highlight relevant variable states and data transformations

**STEP 4: ROOT CAUSE IDENTIFICATION**
- Pinpoint the exact source of the problem
- Explain why this causes the observed behavior
- Discuss any underlying misconceptions or common pitfalls

**STEP 5: SOLUTION**
- Provide the corrected code
- Explain what was changed and why
- Suggest how to prevent similar issues in the future

**STEP 6: LEARNING POINTS**
- Summarize key debugging lessons from this case
- Recommend debugging tools or techniques for similar issues

**CODE TO DEBUG:**
{CODE_BLOCK}

**OBSERVED BEHAVIOR:**
{CURRENT_BEHAVIOR}

**EXPECTED BEHAVIOR:**
{DESIRED_BEHAVIOR}

**ERROR MESSAGE (if any):**
{ERROR_MESSAGE}

Please work through each step methodically, teaching me the debugging process along the way.
```

## Variables to Customize

- `{CODE_BLOCK}`: Paste your Python code here. Include relevant context (imports, function definitions, etc.)
- `{CURRENT_BEHAVIOR}`: Describe what the code is actually doing (e.g., "Returns None instead of a list", "Throws IndexError on line 23")
- `{DESIRED_BEHAVIOR}`: Explain what you expected the code to do (e.g., "Should return a sorted list of unique values")
- `{ERROR_MESSAGE}`: Copy the complete error message if one exists, or write "No error message - logical error" if the code runs but produces wrong results

## Example Input/Output

### Example 1: List Comprehension Bug

**Customized Prompt:**
```
You are a Python debugging expert with a focus on teaching debugging methodology. 

I have Python code that isn't working correctly. Please help me debug it using this systematic approach:

[...full prompt structure...]

**CODE TO DEBUG:**
```python
def get_even_squares(numbers):
    return [x**2 for x in numbers if x**2 % 2 == 0]

result = get_even_squares([1, 2, 3, 4, 5])
print(result)
```

**OBSERVED BEHAVIOR:**
Returns [4, 16] but seems to be missing some values

**EXPECTED BEHAVIOR:**
Should return the squares of all even numbers from the input list

**ERROR MESSAGE (if any):**
No error message - logical error
```

**Output:**
```
STEP 1: INITIAL ANALYSIS
The code runs without errors but returns [4, 16] when we expect it to square the even numbers 
from [1, 2, 3, 4, 5], which should give us [4, 16] (squares of 2 and 4).

Wait - let me reconsider the expected behavior. The issue is in the interpretation...

STEP 2: HYPOTHESIS FORMATION
Most likely cause: The filter condition `x**2 % 2 == 0` is checking if the SQUARE is even, 
not if the original number is even.

This is actually checking: "give me numbers whose squares are even"
Rather than: "give me squares of even numbers"

STEP 3: DIAGNOSTIC INVESTIGATION
Let's trace through:
- x=1: 1**2=1, 1%2=1 (odd) → excluded ✗
- x=2: 2**2=4, 4%2=0 (even) → included ✓
- x=3: 3**2=9, 9%2=1 (odd) → excluded ✗
- x=4: 4**2=16, 16%2=0 (even) → included ✓
- x=5: 5**2=25, 25%2=1 (odd) → excluded ✗

Result: [4, 16] - this is mathematically correct for the current logic!

STEP 4: ROOT CAUSE IDENTIFICATION
The root cause is a logical error in the filter condition. The code filters based on whether 
the SQUARE is even, but any number squared preserves its evenness:
- Even² = Even (e.g., 2²=4, 4²=16)
- Odd² = Odd (e.g., 3²=9, 5²=25)

So `x**2 % 2 == 0` is functionally equivalent to `x % 2 == 0`, but it's doing unnecessary 
computation and the intent is unclear.

STEP 5: SOLUTION

```python
def get_even_squares(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

result = get_even_squares([1, 2, 3, 4, 5])
print(result)  # Output: [4, 16]
```

Changes:
- Changed `if x**2 % 2 == 0` to `if x % 2 == 0`
- Now we filter BEFORE squaring, which is clearer and more efficient
- The logic now clearly states: "take even numbers, then square them"

Prevention: Always check your filter conditions match your intent. Ask yourself: "Am I 
filtering before or after transformation?"

STEP 6: LEARNING POINTS

Key debugging lessons:
1. Trace through with concrete values to see what's actually happening
2. Question whether the code matches the stated intent
3. Mathematical properties matter: even²=even, odd²=odd
4. Filter placement matters: filter → transform vs. transform → filter

Debugging tools for similar issues:
- Use print statements to see intermediate values
- Python Tutor (pythontutor.com) for visualizing execution
- Built-in debugger (pdb) to step through list comprehensions
- Write unit tests with expected inputs/outputs
```

### Example 2: Index Error

**Customized Prompt:**
```
[Prompt with variables filled in for a different scenario involving an IndexError]
```

**Input:**
```python
def get_last_three(items):
    return [items[-1], items[-2], items[-3]]

print(get_last_three([1, 2]))
```

**Output:**
```
[Structured analysis following the same 6-step format, identifying the IndexError when list 
has fewer than 3 elements, explaining negative indexing, and providing a robust solution 
using list slicing: return items[-3:] or return items[max(0, len(items)-3):]
```

## Performance Notes

### Strengths
- Provides educational explanations alongside fixes
- Teaches systematic debugging methodology
- Works well for both syntax and logical errors
- Helps users understand root causes, not just symptoms
- Adapts to different complexity levels

### Limitations
- May be verbose for simple, obvious errors
- Requires clear problem description from user
- Less effective for large codebases (works best with isolated functions)
- Cannot debug runtime environment issues (database connections, file paths, etc.)

### Tips for Best Results
- Provide complete, runnable code when possible
- Include the exact error message with line numbers
- Describe what you've already tried
- Mention your Python experience level for tailored explanations
- For complex issues, isolate the problematic section first
- If dealing with data processing, include sample input data

## Related Prompts
- [Code Reviewer Pro](../coding/code-reviewer-pro.md) - For catching bugs before they happen
- [Python Optimization Expert](../coding/python-optimizer.md) - For improving working code
- [Unit Test Generator](../coding/unit-test-generator.md) - For preventing regressions

## Version History

### v1.0 (2024-01-15)
- Initial version
- Focus on educational debugging methodology
- Six-step systematic approach
- Emphasis on teaching alongside fixing
