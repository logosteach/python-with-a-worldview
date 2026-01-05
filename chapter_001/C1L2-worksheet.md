<script type="text/javascript" 
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

# Worksheet - C1L2

## Printing and Escape Characters

## Instructions
This worksheet builds on your knowledge from Lesson 1 (data types: int, float, str; variable assignment; naming conventions; `type()` function; order of operations) and introduces new concepts from Lesson 2: the `print()` function, generating basic errors, escape characters (`\n`, `\t`, `\'`), string multipliers, and white space. Complete the exercises below in a Python script or notebook. Do **not** use type conversion functions (`int()`, `float()`, `str()`) as these have not been covered.

## Part 1: The `print()` Function
1. **Basic Printing**  
   Write Python code to:  
   a. Print your name as a string.  
   b. Print your age as an integer.  
   c. Print your height in meters as a float.  
   d. Print a sentence combining all three, e.g., "My name is Alex, I am 25 years old, and my height is 1.75 meters."

2. **Multiple Prints**  
   Write Python code to print the following on separate lines using a single `print()` statement:  
   - "Welcome to Python!"  
   - "This is fun!"  
   - "Let's learn more!"

## Part 2: Generating Basic Errors
3. **Error Exploration**  
   Write Python code that intentionally causes the following errors. After running each, explain what caused the error and how to fix it.  
   a. A `NameError` (e.g., using an undefined variable).  
   b. A `SyntaxError` (e.g., incorrect syntax like a missing parenthesis).  
   c. A `ZeroDivisionError` (e.g., dividing by zero).  

::: page-break :::

## Part 3: Escape Characters
4. **Using Escape Characters**  
   Write Python code to:  
   a. Print a string with a newline (`\n`) to display "Hello" and "World" on separate lines.  
   b. Print a string with a tab (`\t`) to display "Name: Alex" with a tab between "Name:" and "Alex".  
   c. Print a string using single quotes that includes an apostrophe, e.g., "It's a great day!" using the `\'` escape character.

5. **Creative Use of Escape Characters**  
   Write Python code to print the following exactly as shown (including spacing):  
```
Item        Price
Apple       0.50
Banana      0.75
```

## Part 4: String Multipliers
6. **String Multiplier Practice**  
   Write Python code to:  
   a. Print the string "Hi!" five times in a row (e.g., "Hi!Hi!Hi!Hi!Hi!") using a string multiplier.  
   b. Print a line of 10 asterisks (`**********`) using a string multiplier.  
   c. Combine a string multiplier with a newline (`\n`) to print "Hello" three times, each on a new line.

## Part 5: White Space
7. **Understanding White Space**  
   Explain how white space affects the following code snippets. Then, run them and describe the output.  
a. 
```python
print("Hello   World")
```
b. 
```python
print("Hello\tWorld")
```

::: page-break :::

c. 
```python
print("Hello\nWorld")
```

8. **Formatting with White Space and Multipliers**  
   Write Python code to print a simple box-like structure using string multipliers and white space, like this:  
```
******
*    *
*    *
******
```

## Part 6: Mixed Practice
9. **Debug the Code**  
   The following code has errors related to escape characters, string multipliers, or the `print()` function. Fix the issues and explain what was wrong.  
```python
message = "Welcome to Python!"
print(message * 2 + \n + "Done!")
```

10. **Combined Concepts**  
    Write Python code to:  
    a. Create a variable `item_name` with the value `"Pizza"`.  
    b. Create a variable `price` with the value `9.99`.  
    c. Use a single `print()` statement with escape characters and a string multiplier to display:  
```
Item: Pizza
Price: $9.99
--------------------
```

## Submission
Write your answers and Python code in a script or notebook. Include comments to explain your work. Submit your completed worksheet to your instructor.

&copy; 2025 [LogosTeach](https://www.logosteach.com) - All Rights Reserved