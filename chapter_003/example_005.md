### Example: Using `*args` (Variable Arguments) in a Python Function

```python
# Function that can accept ANY number of numbers and returns their average
# Here we use *args to collect all extra arguments into a tuple
def calculate_average(name, *scores):
    """
    Parameters:
    - name:        required (normal parameter) - student's name
    - *scores:     variable arguments - any number of test scores (0 or more)
    """
    if not scores:                    # Check if no scores were provided
        return f"{name} has no scores yet."
    
    total = sum(scores)               # *scores is a tuple, so sum() works
    count = len(scores)
    average = total / count
    
    return f"{name}'s average score is {average:.1f}"

# --- Different ways to call the function ---

# 1. Just the required parameter (no scores)
print(calculate_average("Emma"))
# Output: Emma has no scores yet.

# 2. One score
print(calculate_average("Liam", 85))
# Output: Liam's average score is 85.0

# 3. Multiple scores
print(calculate_average("Sophia", 92, 88, 95, 79))
# Output: Sophia's average score is 88.5

# 4. Using a list with unpacking (*)
test_scores = [100, 95, 98]
print(calculate_average("Noah", *test_scores))
# Output: Noah's average score is 97.7
```

### Important Rule: Ordering of Parameters

When using `*args` (or `**kwargs`), **Python enforces a strict order** for parameters:

```python
# Correct order:
def good_function(a, b, *args, c=10, **kwargs):
    pass

# WRONG orders - these will cause SyntaxError!
def bad1(*args, a):                  # Variable args BEFORE normal args → ERROR
    pass

def bad2(a, *args, b, c):            # Normal required param AFTER *args → ERROR
    pass
```

**Correct order summary (must follow this sequence):**

1. Normal (required) parameters  
2. Default/optional parameters  
3. `*args` (variable positional arguments)  
4. Keyword-only parameters (if any)  
5. `**kwargs` (variable keyword arguments)

**Why this order matters**  
Python reads arguments from left to right when you call the function.  
If `*args` came before a normal parameter, Python wouldn’t know where the `*args` tuple ends and the next required argument begins → it creates ambiguity → SyntaxError.

**Quick beginner takeaway:**  
Think of it like reading a sentence: you have to put the main words first, then any extra words (*args), then optional details, and finally any "named" extras (**kwargs).

Play around with this function — try giving it 0, 1, 5, or 10 scores and see how flexible `*args` makes it! 🚀