### Example: Creating a user-defined function that formats a name (proper capitalization)

```python
# Function to format a name with proper capitalization
def format_name(first_name, last_name):
    # Capitalize the first letter and make the rest lowercase
    formatted_first = first_name.capitalize()
    formatted_last = last_name.capitalize()
    
    # Combine them into a full name
    full_name = formatted_first + " " + formatted_last
    
    return full_name

# --- Examples of using the function ---
print(format_name("joHn", "doE"))          
# Output: John Doe

print(format_name("mAry", "ANN"))          
# Output: Mary Ann

print(format_name("alexander", "Hamilton")) 
# Output: Alexander Hamilton

# You can also store and use the result
user_first = "sophia"
user_last = "garcia-rodriguez"
nice_name = format_name(user_first, user_last)
print("Welcome,", nice_name + "!")
# Output: Welcome, Sophia Garcia-rodriguez!
```

**Quick explanation for beginners:**
- The function takes **two parameters**: `first_name` and `last_name`
- `.capitalize()` is a built-in string method that:
  - Makes the first character uppercase
  - Makes all other characters lowercase
- We use `+` to join the formatted parts with a space in between
- `return` sends the nicely formatted full name back to the caller

**Bonus tip:**  
This simple version works great for most names, but if you have names like "McDonald" or "O'Connor", you might want a more advanced version later. For now, this is perfect for learning functions! 😊

Try calling it with your own name (even if you type it in all lowercase or all caps)!