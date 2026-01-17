Here are the **complete solutions** to the Python Functions Computer Lab exercises — all in clean markdown format.

Feel free to copy them, run them, and compare with your own attempts!

### Python Functions Computer Lab – Solutions

#### Problem 1 – Warm-up (Basic function + return)

```python
def double_it(number):
    return number * 2

# Test it
print(double_it(5))     # 10
print(double_it(-3))    # -6
print(double_it(0))     # 0
```

#### Problem 2 – Temperature Converter

```python
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Test examples
print(f"32°F = {fahrenheit_to_celsius(32):.1f}°C")      # 0.0°C
print(f"212°F = {fahrenheit_to_celsius(212):.1f}°C")    # 100.0°C
print(f"68°F = {fahrenheit_to_celsius(68):.1f}°C")      # 20.0°C
```

#### Problem 3 – Name Formatter with Default

```python
def make_full_name(first, last, middle=""):
    formatted_first = first.capitalize()
    formatted_last = last.capitalize()
    
    if middle:
        formatted_middle = middle.capitalize()
        return f"{formatted_first} {formatted_middle} {formatted_last}"
    else:
        return f"{formatted_first} {formatted_last}"

# Tests
print(make_full_name("alex", "smith"))                  # Alex Smith
print(make_full_name("luna", "rivera", "mae"))          # Luna Mae Rivera
print(make_full_name("NOAH", "KIM", "ji-hoon"))         # Noah Ji-hoon Kim
```

#### Problem 4 – Placeholder Function (using `pass`)

```python
def send_email(to, subject, message):
    """
    Placeholder function for sending emails.
    Will be implemented later with actual email-sending logic
    (e.g., using smtplib or an email API).
    """
    pass

# Calling it does nothing (which is intentional)
send_email(
    "friend@example.com",
    "Happy Birthday!",
    "Hope you have an awesome day!"
)
print("Email function ready for future use!")
```

#### Problem 5 – Flexible Score Tracker (using `*args`)

```python
def best_score(player_name, *scores):
    if not scores:
        return f"No scores recorded for {player_name} yet."
    
    best = max(scores)
    return f"{player_name}'s best score is {best}"

# Test cases
print(best_score("Maya"))                       # No scores...
print(best_score("Liam", 72))                   # Liam's best score is 72
print(best_score("Sophia", 88, 95, 91, 84))     # Sophia's best score is 95
```

#### Problem 6 – Personalized Message Builder (using `**kwargs`)

```python
def build_profile(name, **info):
    print(f"Profile for {name.capitalize()}:")
    
    if not info:
        print("  (no extra details provided)")
    else:
        for key, value in info.items():
            pretty_key = key.replace("_", " ").title()
            print(f"- {pretty_key}: {value}")
    
    print()  # empty line for readability

# Tests
build_profile("sophia")
build_profile("max", age=11, city="Portland", favorite_game="Minecraft")
build_profile("luna", pet="cat", favorite_color="purple", school="Lincoln")
```

#### Problem 7 – Combined Challenge (mix everything!)

```python
def party_invitation(host, time="7:00 PM", *guests, **party_details):
    invitation = f"You're invited to {host}'s party!\n"
    invitation += f"Time: {time}\n"
    
    if guests:
        invitation += f"Guests: {', '.join(guests)}\n"
    
    for key, value in party_details.items():
        pretty_key = key.replace("_", " ").title()
        invitation += f"{pretty_key}: {value}\n"
    
    return invitation

# Example usage
print(party_invitation("Noah", "8:30 PM", "Luna", "Max", "Emma",
                      theme="Neon Glow", location="Backyard"))

# Another example with default time
print(party_invitation("Emma", "Ava", "Liam", food="Pizza & Cake"))
```

#### Problem 8 – The Ultimate Mini Project

```python
def describe_pet(name, animal_type="dog", **details):
    description = f"{name.capitalize()} is a {animal_type.lower()}"
    
    if details:
        description += " who"
        items = []
        for key, value in details.items():
            pretty_key = key.replace("_", " ")
            items.append(f"{pretty_key} {value}")
        description += " " + ", ".join(items)
    
    description += "."
    return description

# Test cases
print(describe_pet("Whiskers", "cat", age=3, color="gray", likes="chasing lasers"))
# Whiskers is a cat who age 3, color gray, likes chasing lasers.

print(describe_pet("Buddy"))
# Buddy is a dog.

print(describe_pet("Mochi", "rabbit", favorite_food="carrots", age=2))
# Mochi is a rabbit who favorite food carrots, age 2.
```

Great job getting through the whole lab!

Which problem(s) were the most challenging or interesting for you?  
Want to make any of them harder, add error checking, or try a new variation? 😊