Here’s a fun **Python Function Practice Lab** designed for beginners!  
Think of this as your “Computer Lab” session — complete these 8 exercises to master functions, parameters, return, defaults, `*args`, `**kwargs`, and `pass`.

Copy the problems into your editor, try to solve them yourself first, then check the hints or example solutions at the bottom (but only after you’ve tried!).

### Python Functions Computer Lab – Level: Beginner

**Instructions:**  
For each problem, write a function that does what is asked.  
Test your function with at least 2–3 different examples.

---

**Problem 1 – Warm-up (Basic function + return)**  
Write a function called `double_it` that takes one number and **returns** double that number.

---

**Problem 2 – Temperature Converter**  
Write a function called `fahrenheit_to_celsius` that takes a temperature in Fahrenheit and **returns** the temperature in Celsius.  
Formula: `C = (F - 32) × 5/9`

---

**Problem 3 – Name Formatter with Default**  
Write a function called `make_full_name` that takes:  
- `first` (required)  
- `last` (required)  
- `middle=""` (default empty string)  

It should return the full name with proper capitalization (like our earlier example).  
If middle name is given, include it.

Example calls:  
```python
make_full_name("alex", "smith")                 → "Alex Smith"
make_full_name("luna", "rivera", "mae")         → "Luna Mae Rivera"
```

---

**Problem 4 – Placeholder Function (using `pass`)**  
Create a function called `send_email` that takes:  
- `to`  
- `subject`  
- `message`  

For now, the function should do **nothing** (just use `pass`).  
Add a docstring explaining that this is a placeholder for future email sending code.

---

**Problem 5 – Flexible Score Tracker (using `*args`)**  
Write a function called `best_score` that takes:  
- `player_name` (required)  
- any number of scores using `*args`  

It should return a string like:  
`"Maya's best score is 98"`

If no scores are given, return: `"No scores recorded for [name] yet."`

---

**Problem 6 – Personalized Message Builder (using `**kwargs`)**  
Write a function called `build_profile` that takes:  
- `name` (required)  
- any number of extra keyword arguments (`**info`)  

It should print (not return) a nice little profile card like this:

```
Profile for Sophia:
- Age: 13
- City: Portland
- Favorite Game: Minecraft
```

If no extra info is given, just print:  
`Profile for [name]: (no extra details provided)`

---

**Problem 7 – Combined Challenge (mix everything!)**  
Write a function called `party_invitation` that takes:  
- `host` (required)  
- `time` (default "7:00 PM")  
- `*guests` (variable number of guest names)  
- `**party_details` (any extra info like location, theme, etc.)

It should **return** a formatted invitation string.

Example:
```python
print(party_invitation("Noah", "8:30 PM", "Luna", "Max", "Emma", theme="Neon Glow", location="Backyard"))
```

Possible output:
```
You're invited to Noah's party!
Time: 8:30 PM
Guests: Luna, Max, Emma
Theme: Neon Glow
Location: Backyard
```

---

**Problem 8 – The Ultimate Mini Project**  
Write a function called `describe_pet` that:  
- Takes `name` (required)  
- Takes `animal_type="dog"` (default)  
- Takes any extra details using `**details`  
- Returns a nice description string

Example calls:
```python
describe_pet("Whiskers", "cat", age=3, color="gray", likes="chasing lasers")
describe_pet("Buddy")  # should use default animal_type="dog"
```

---

### Quick Hints & Solution Ideas (look only after trying!)

1. Just `return number * 2`
2. Remember parentheses and division → watch for integer division!
3. Use `.capitalize()` and check `if middle:`
4. Docstring + `pass` = perfect placeholder
5. `if not scores:` for empty case, otherwise `max(scores)`
6. Loop through `info.items()` like we did in the greeting example
7. Build the string with f-strings and conditionals
8. Very similar to problem 6, but return instead of print

Have fun coding in the lab, John!  
Which problem do you want to start with, or would you like a full solution + explanation for one of them? 🚀