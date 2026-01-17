### Example: Function to format a name with an **optional** middle name (using a default parameter)

```python
# Function to format a name with proper capitalization
# The middle_name parameter has a DEFAULT VALUE of "" (empty string)
# This means: if the caller doesn't provide a middle name, Python automatically uses ""
def format_name(first_name, last_name, middle_name=""):
    # Capitalize first letter and make the rest lowercase for each part
    formatted_first = first_name.capitalize()
    formatted_last = last_name.capitalize()
    
    # Only include middle name if something was actually provided
    # (an empty string is considered "falsey" in Python, so this check works nicely)
    if middle_name:
        formatted_middle = middle_name.capitalize()
        full_name = f"{formatted_first} {formatted_middle} {formatted_last}"
    else:
        # If no middle name was given (or it was ""), we skip it
        full_name = f"{formatted_first} {formatted_last}"
    
    return full_name

# --- Examples of using the function ---

# 1. Calling with only 2 arguments → middle_name uses its default value ("")
print(format_name("joHn", "doE"))           # middle_name = "" automatically
# Output: John Doe

print(format_name("mAry", "ANN"))
# Output: Mary Ann

# 2. Calling with 3 arguments → we override the default value
print(format_name("alexander", "Hamilton", "the great"))
# Output: Alexander The Great Hamilton

print(format_name("sophia", "garcia", "marie"))
# Output: Sophia Marie Garcia

# 3. Using keyword arguments (great for clarity with defaults!)
print(format_name(first_name="james", last_name="kirk", middle_name="tiberius"))
# Output: James Tiberius Kirk

# Bonus: Even crazy input gets cleaned up nicely
print(format_name("ELON", "musk", "reeve"))
# Output: Elon Reeve Musk
```

**Quick explanation for beginners – What is a default parameter?**

- A **default parameter** lets you give a parameter a value right in the function definition  
  → `middle_name=""` means: "If no middle name is passed, pretend the user sent an empty string"
- This makes the function **more flexible**:
  - You can call it with fewer arguments when you don’t need the optional part
  - Very common in real Python code (many built-in functions use defaults too!)
- Default values are only used when the argument is **not** provided
- Important rule: Default parameters must come **after** regular (required) parameters in the function definition

Try calling the function both ways — with and without a middle name — and watch how Python handles the default automatically! 😊