---
math: true
---

# Worksheet - C1L7

## More About Strings

**Instructions:** Answer the questions below. For code-related questions, write your Python code in the provided spaces (you can test in your IDE). This worksheet reviews and applies concepts from the lesson, including previous topics like variables, data types, print, f-strings, casting, and new ones like string methods, immutability, referencing, indexing, slicing, strip/rstrip, replace, and len().

Name: _______________________ Date: ____________

---

### Part 1: Understanding String Immutability

**Question:** 

Explain what string immutability means in Python, and why it matters when working with string variables.

Then, consider this code snippet:

```python
greeting = "Hello"
greeting[0] = "J"  # Trying to change the first character
print(greeting)
```

a. What do you think will happen when this code runs? Why?
b. How could you "change" the string to make it "Jello" without directly modifying the original (hint: think about assignment and referencing)? Write the corrected code below.

```python
# Your code goes here
```

### Part 2: String Methods and Immutability

**Question:**

The `replace()` method is a behavior of strings that can create a new version of the string with certain changes. Some students might think that calling `replace()` directly changes the original string variable.
Consider this code snippet:

```python
message = "Hello, world!"
message.replace("world", "Python")
print(message)
```

a. What will this code output? Why? (Explain in terms of immutability.)
b. How would you modify the code to actually update the `message` variable to say "Hello, Python!"? Write the corrected code below, and explain the role of assignment/referencing here.

```python
# Your code goes here
```

### Part 3: String Slicing Misconceptions

**Question:** 

String slicing allows you to extract parts of a string using indices, but beginners often misunderstand the off-by-one behavior: the end index is exclusive (not included in the slice).
Consider this code snippet and common mistake:

```python
fruit = "banana"
slice1 = fruit[1:3]  # Intended to get "ana"? 
print(slice1)
```

a. What will this code actually output? Why? (Explain the start and end indices, including off-by-one.)
b. A student wants the slice to be characters from position 2 to 4 (1-based counting: 'a' at 2, 'n' at 3, 'a' at 4). What indices should they use instead, and why? Write the correct code and predict the output.

```python
# Your code goes here
```

c. If forgotten, what misconception might lead to an error like including an extra character or missing one? Give an example with "Python" string aiming for "yth" but getting it wrong.

### Part 4: Understanding the `len()` function

**Question:**

The `len()` function returns the length (number of characters) in a string, which is useful for indexing, slicing, and avoiding off-by-one errors.

Consider this code snippet with a potential misconception (students might think len() excludes spaces or counts from 1 instead of the actual character count):

```python
text = "Python!"
length = len(text)
print(length)
```

a. What will this code output? Why? (Count the characters manually to confirm, including any special ones.)

b. How could you use `len()` to safely slice the last 3 characters from `text` without hardcoding indices? Write the code below and predict the output.

```python
# Your code goes here
```

### Part 5: Understanding `strip()`, `lstrip()` and `rstrip()`

**Question:**

The `strip()` method removes whitespaces (spaces, tabs, newlines) from both ends of a string, `lstrip()` from the left only, and `rstrip()` from the right only. Like other methods, they return a new string due to immutability and don't change the original unless reassigned. Students might assume they remove all internal spaces or modify in place.

Consider the code snippet with user input simulation:

```python
user_input = "   Hello, Python!   "
cleaned = user_input.strip()
print(cleaned)
```

a. What will this code output? Why? (Describe what `strip()` does to leading/trailing spaces.)
b. Predict the outputs for the following without running (explain differences):
- `user_input.lstrip()`
- `user_input.rstrip()`
- `user_input.strip("!")` # Note: strip can take arguments for custom chars.

Write the predicted outputs below.

c. Write code to remove only trailing spaces and then use replace() to change "Python" to "World", storing in a new variable. Explain why the original `user_input` remains unchanged (tie to immutability and referencing).

```python
# Your code goes here
```

::: page-break :::

### Part 6: Indexing Single Characters

**Question:**

Strings can be indexed to access single characters using [index], starting from 0. Students might confuse this with 1-based counting or think it modifies the string.

Consider this code snippet:

```python
language = "Python"
first_char = language[0]
third_char = language[2]
print(first_char, third_char)
```

a. What will this code output? Why? (Explain zero-based indexing with examples from the string positions: P at 0, y at 1, etc.)

b. Write code to get the middle character "Hello" (index 2). What if the string was "Hi" (even length)- what index would you use for one of the middles, and how might `len()` help find it dynamically?

```python
# Your code here for "Hello"
# Dynamic example with len() 
```

c. A common error: Trying language[6] on "Python" (length 6). What happens? Fix it using `len()` safely get the last character without hardcoding (hint: `len() - 1`), and tie to off-by-one (valid indices: 0 to `len() - 1`).

```python
# Your safe code goes here
```

<footer>
&copy; 2026 <a href="https://www.logosteach.com">LogosTeach</a> - All Rights Reserved
</footer>