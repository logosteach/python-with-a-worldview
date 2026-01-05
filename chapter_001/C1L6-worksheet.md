<script type="text/javascript" 
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

# Worksheet - C1L6

## Comments

## Instructions
This worksheet builds on your knowledge from previous lessons (data types, variables, `print()`, f-strings, division, type conversions, etc.) and introduces comments: inline comments (  (using `#` on the same line as code) and paragraph (multi-line) comments (using triple quotes `"""` or triple single quotes `'''` for documentation). Use comments extensively in your code to explain your thought process. Complete the exercises below in a Python script or notebook. Remember: comments are ignored by Python but help humans understand code.

## Part 1: Inline Comments
1. **Basic Inline Comments**  
   Add inline comments to explain each line of the following code:  
```python
radius = 5.0
area = 3.14 * radius ** 2
print(f"Area is {area}")
```  
Example: `radius = 5.0  # Assign float value for radius`

2. **Comment Operations**  
   Write code to calculate perimeter of a rectangle (length 10, width 5), with inline comments:  
   - Comment variable assignments  
   - Comment the calculation using order of operations  
   - Comment the print statement with f-string

## Part 2: Paragraph Comments
3. **Multi-Line Documentation**  
   You can use comments to explain the purpose and meaning of a program.

   Use a paragraph comment (""" """) at the top of a code block to explain:  
   a. What the script does (e.g., "This script calculates and prints BMI using height and weight.").  
   Then write the code with variables `weight = 70`, `height = 1.75`, `bmi = weight / height ** 2`, print formatted to 2 decimals.  
   b. Add another paragraph comment before the print to describe formatting.

::: page-break :::

1. **Sectioning with Comments** 

You can use comments to section a program into more readable parts.

Write code for type conversions (str to int, etc.), use paragraph comments to separate sections: 

```python 
"""
Section 1: String to Number Conversions
"""
### Code here  
"""
Section 2: Calculations
"""
```

## Part 3: Combining Comments with Previous Concepts
5. **Commented Division and Modulo**  
   Use inline and paragraph comments in code:  
   """  
   This block demonstrates division types with explanations.  
   """  
   a = 10 / 3  # Float division  
   b = 10 // 3  # Floor division  
   c = 10 % 3  # Modulo  
   print(f"Results: {a:.2f}, {b}, {c}")

6. **Error Prevention with Comments**  
   Add comments explaining potential errors:  
   ### int("abc") would cause ValueError - invalid literal  
   ### So we use valid strings only  
   num = int("100")  # Safe conversion  
   Also add a paragraph comment on why we comment errors.

## Part 4: Formatting and Comments
7. **Commented f-Strings**  
   Use f-strings with padding/precision, add inline comments:  
   price = 9.99  
  quantity = 3  
   total = price * quantity  # Calculate total  
   print(f"Total: ${total:>8.2f}")  # Right-align, 2 decimals

8. **Debug with Comments**  
   The code has no runtime errors but improve with comments:  
```python
seconds = 3665
minutes = seconds // 60
secs_left = seconds % 60
print(minutes, secs_left)
```  
   Add paragraph comment explaining time conversion, inline for ops.

## Part 5: Mixed Practice
9. **Fully Commented Script**  
   Write a complete script with:  
   - Paragraph comment at top: script purpose (convert temperature C to F).  
   - Inline comments on each line.  
   Code: `celsius = 25`, `fahrenheit = celsius * 9/5 + 32`, print formatted.  
   Use conversions if needed (e.g., str for output).

10. **Comment Challenge**  
    Debug this poorly commented code by adding explanations:  
```python
x = "10"
y = int(x)
z = y / 2
print(z)
```  
    Add paragraph on conversion risks, inline on each step. Then fix if needed (use // for int result?).

## Submission
Write your answers and Python code in a script or notebook. Ensure every code block has appropriate comments (aim for clarity). Submit your completed worksheet to your instructor.