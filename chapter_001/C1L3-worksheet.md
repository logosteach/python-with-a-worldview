<script type="text/javascript" 
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

# Worksheet - C1L3

## F-Strings

## Instructions
This worksheet builds on your knowledge from previous lessons (data types, variables, `print()`, escape characters, string multipliers, errors, etc.) and introduces new concepts: f-strings, padding and alignment in formatted output, and controlling decimal precision. Complete the exercises below in a Python script or notebook. Use f-strings where appropriate to practice the new concepts.

## Part 1: Introduction to f-Strings
1. **Basic f-String Usage**  
Write Python code using f-strings to:  
a. Create variables `name = "Alice"`, `age = 30`, and print: "My name is Alice and I am 30 years old."  
b. Create variables `length = 5.5`, `width = 3.0`, and print the area: "The area is 16.5" (calculate area as length * width).  
c. Combine a string and a calculation in one f-string: Print "5 squared is 25" using a variable for the base.

1. **f-Strings vs. Concatenation**  
Rewrite the following using concatenation (+), then rewrite again using an f-string. Explain which is easier and why.  
```python
product = "Book"
price = 12.99
# Original goal: Print "The Book costs $12.99"
```

## Part 2: Padding and Alignment
3. **Padding with Spaces**  
Use f-strings with padding to format the following output exactly (assume variables `item1 = "Apple"`, `price1 = 0.5`, etc.):  
```
Item    Price
Apple   $ 0.50
Banana  $ 0.75
Cherry  $ 1.20
```  
Use width specifiers like `:10` for alignment. Experiment with left, right, and center alignment (^).

4. **Alignment Practice**  
Write code to print a table header like this using center alignment and padding:  
```
    Name     |    Age    |   Height  
```  
Use a width of 10 for each column and pipes for separators.

## Part 3: Decimal Precision
5. **Controlling Decimals**  
Use f-strings with precision specifiers to:  
a. Set `pi = 3.14159` and print "Pi to 2 decimals: 3.14" using `.2f`.  
b. Set `value = 123.45678` and print with 3 decimal places: "123.457" (note rounding).  
c. Set `small = 0.123456` and print with 1 decimal place: "0.1".

6. **Combining Precision and Padding**  
Format a price list with right-aligned prices padded to 8 characters and 2 decimal places:  
```
Item: Apple     Price: $   0.50
Item: Banana    Price: $   0.75
```  
Use variables for items and prices.

## Part 4: Mixed Practice with Previous Concepts
7. **Error Handling in Formatting**  
Intentionally cause a `ValueError` or `SyntaxError` in an f-string (e.g., mismatched braces). Write the bad code, explain the error, and fix it.

8. **Creative Formatting**  
Use f-strings, multipliers, escape characters (\n, \t), padding, alignment, and precision to print a "receipt" like:  
```
*** Receipt ***
Item     Qty   Price   Total
Pizza      2   $9.99  $19.98
Soda       3   $1.50   $4.50
------------------------
Grand Total:         $24.48
```  
Calculate totals using variables and order of operations.

::: page-break :::

## Part 5: Debug the Code
9. **Debug Formatting Issues**  
   The following code has issues with f-strings, padding, or precision. Fix and explain.  
```python
name = "Bob"
score = 95.678
print(f"Name: {name:10} Score: {score:3f}")
```

10. **Combined Challenges**  
Write code to:  
a. Use variables `radius = 2.5`, calculate area = 3.14159 * radius ** 2.  
b. Print using f-string with \n, padding, and 2 decimal places:  
```
Circle Area Calculator
Radius:  2.50
Area:   19.63
```

## Submission
Write your answers and Python code in a script or notebook. Include comments explaining your formatting choices. Submit your completed worksheet to your instructor.

&copy; 2025 LogosTeach - All Rights Reserved