**Here’s a super beginner-friendly example that explains `**kwargs` in a simple, clear way!**

### Example: Understanding `**kwargs` – Extra Named Arguments

```python
# What is **kwargs? 
# It’s a special way to let someone give your function as MANY extra named arguments as they want
# The two asterisks ** turn those extra name=value pairs into a dictionary inside your function
# "kwargs" just stands for "keyword arguments" – it's the name most Python people use

def introduce_friend(name, **extra_info):
    """
    This function says hi to a friend and shares any extra details they give us.
    - name is required (must always be given)
    - **extra_info can be zero or many extra things like age=12, city="Portland", etc.
    """
    
    # Start with a basic greeting
    message = f"Hi everyone! This is my friend {name.capitalize()}!"
    
    # If they gave us any extra info (**extra_info is a dictionary!)
    if extra_info:
        message += "\nHere are some cool things about them:"
        
        # Loop through the dictionary to show each piece of info
        for key, value in extra_info.items():
            # Make the key look pretty (replace _ with space and capitalize)
            pretty_key = key.replace("_", " ").title()
            message += f"\n- {pretty_key}: {value}"
    
    # Show the final message
    print(message)
    print("-" * 50)   # just a nice separator line


# Let's try it out!

# 1. Just the name – no extra info
introduce_friend("luna")
# Output:
# Hi everyone! This is my friend Luna!
# --------------------------------------------------

# 2. Add one extra piece of info
introduce_friend("max", age=11)
# Output:
# Hi everyone! This is my friend Max!
# Here are some cool things about them:
# - Age: 11
# --------------------------------------------------

# 3. Add several extra details – **kwargs collects them all!
introduce_friend(
    "sophia",
    favorite_game="Minecraft",
    pet="cat named Whiskers",
    city="Portland",
    dream_job="game designer"
)
# Output:
# Hi everyone! This is my friend Sophia!
# Here are some cool things about them:
# - Favorite Game: Minecraft
# - Pet: cat named Whiskers
# - City: Portland
# - Dream Job: game designer
# --------------------------------------------------

# 4. You can even pass a whole dictionary using ** (unpacking)
info = {
    "favorite_color": "purple",
    "sport": "soccer"
}
introduce_friend("noah", **info)
# Output:
# Hi everyone! This is my friend Noah!
# Here are some cool things about them:
# - Favorite Color: purple
# - Sport: soccer
# --------------------------------------------------
```

### Super Simple Explanation for New Coders

- Normal parameters: You **must** give them (like `name`)
- Default parameters: You **can** give them (like `age=10`)
- `*args`: Catches **any number** of extra **normal** arguments (no names)
- `**kwargs`: Catches **any number** of extra **named** arguments (with = sign)

Think of `**kwargs` like a magic notebook:  
Anyone can write as many notes as they want in the form `thing=value`,  
and your function gets to read all of them as a dictionary! 📓✨

### Quick Memory Trick
- `*args` → "a bunch of regular arguments" (like a list of unnamed gifts)
- `**kwargs` → "a bunch of named gifts with labels" (each one has a name tag)

Have fun experimenting — try adding your own favorite things about a friend! 😊