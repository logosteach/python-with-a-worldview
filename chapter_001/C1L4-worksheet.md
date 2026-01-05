<script type="text/javascript" 
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

# Worksheet - C1L4

## Division in Python

## Instructions
This worksheet builds on your knowledge from previous lessons (data types, variables, `print()`, f-strings, order of operations, etc.) and introduces the three types of division in Python: `/` (float division), `//` (floor division), and `%` (modulo). Complete the exercises below in a Python script or notebook. Use f-strings for output where appropriate to practice formatting.

## Part 1: Understanding Division Types
1. **Basic Division Operations**  
   For each pair of numbers, calculate by hand and then use Python to confirm:  
   a. `10 / 3`, `10 // 3`, `10 % 3`  
   b. `20 / 4`, `20 // 4`, `20 % 4`  
   c. `7 / 2`, `7 // 2`, `7 % 2`  
   Explain the difference: `/` always returns a float, `//` returns the integer floor, `%` returns the remainder.

2. **Type Observation**  
   Use the `type()` function to check the data type of the results from:  
   a. `10 / 3`  
   b. `10 // 3`  
   c. `10 % 3`  
   Print the results using f-strings, e.g., "10 / 3 is {result} and type is {type(result)}".

## Part 2: Float vs. Floor Division
3. **Practical Examples**  
   Write Python code to:  
   a. Calculate average speed: distance = 100 km, time = 3.5 hours. Use `/` and print with 2 decimal places: "Average speed: 28.57 km/h".  
   b. Divide 17 apples among 5 people: Use `//` for apples each gets, `%` for leftovers. Print: "Each gets 3 apples, 2 left over."  
   c. Convert 100.75 dollars to dollars and cents: Use `//` for dollars, and calculate cents from remainder (hint: multiply remainder by 100 and use `//` again).

::: page-break :::

4. **Order of Operations with Division**  
   Evaluate by hand, then code:  
   a. `10 + 20 / 5`  
   b. `(10 + 20) // 5`  
   c. `17 % 5 * 2`  
   Use parentheses to change outcomes and explain differences.

## Part 3: Modulo Operator
5. **Even/Odd Check**  
   Write code to check if a number is even or odd using `%`.  
   a. Set `num = 10`, print "Even" if `num % 2 == 0`, else "Odd". Use f-string.  
   b. Repeat for `num = 7`.  
   c. Explain how modulo helps in parity checks.

6. **Remainder Applications**  
   Use modulo to:  
   a. Find last digit of 12345 (use `% 10`).  
   b. Check if 100 is divisible by 7 (remainder == 0).  
   c. Cycle through days: (day_number % 7) to get weekday index.

## Part 4: Formatting with Division Results
7. **Padding and Precision with Division**  
   Use f-strings with alignment, padding, and precision:  
   a. For values from 10/3, 20//4, etc., format a table:  

&copy; 2025 [LogosTeach](https://www.logosteach.com) - All Rights Reserved