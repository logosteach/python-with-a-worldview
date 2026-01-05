<script type="text/javascript" 
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

# Worksheet - C1L5

## Integers, Floats, and Strings, "Oh My!"

## Instructions
This worksheet builds on your knowledge from previous lessons (data types, variables, `print()`, f-strings, division operators, order of operations, etc.) and introduces type conversion functions: `int()`, `float()`, and `str()`. You may now use these for conversions, but do **not** use loops or the `input()` function yet. Complete the exercises below in a Python script or notebook. Use f-strings for formatted output.

## Part 1: Understanding Type Conversions
1. **Basic Conversions**  
   Write Python code to:  
   a. Convert the float `3.14` to an integer using `int()` and print the result (should be 3). Explain truncation.  
   b. Convert the string `"100"` to an integer using `int()` and add 5, print: "105".  
   c. Convert the integer `42` to a float using `float()` and print with 1 decimal: "42.0".  
   d. Convert the float `9.99` to a string using `str()` and print: "Price: 9.99".  
   Use `type()` to confirm types after conversion.

2. **Conversion Results and Types**  
   Predict the output and type, then code to verify:  
   a. `int("25") + 10`  
   b. `float("3.5") * 2`  
   c. `str(100 / 4)`  
   Explain why `int("3.14")` would cause an error (ValueError).

## Part 2: Practical Conversions with Operations
3. **Mixing Types Safely**  
   Write code to:  
   a. Set `price = "12.50"` (str), convert to float, add tax (multiply by 1.08), print rounded result with f-string: "Total: 13.50" (use `.2f`).  
   b. Set `age = 25` (int), convert to str, concatenate with " years old", print.  
   c. Set `height = 1.75` (float), convert to int (meters to approximate cm? Wait, better: multiply by 100 first, then int), print "175 cm".

::: page-break :::

4. **Division and Conversion**  
   Use division operators with conversions:  
   a. Convert `10 // 3` to float, print "3.0".  
   b. Take `17 % 5`, convert to str, print "Remainder as string: '2'".  
   c. Calculate `100 / 6`, convert to int (floor manually), compare to `//`.

## Part 3: Formatting Converted Values
5. **Padding, Precision, and Conversions**  
   Use f-strings with conversions:  
   a. Set `score = 95.678`, convert to str with precision? (Wait, format in f: but practice str(int(score))). Print padded: "Score:     95" (right-align 5 chars).  
   b. Convert `3.14159` to str with slicing or just format: but use `f"{float_num:.2f}"` then pad.  
   c. Create table of conversions:  

&copy; 2026 [LogosTeach](https://www.logosteach.com) - All Rights Reserved