## Unit 2: Control Flow and Iteration in Python

### 1. Conditional Statements
- **Review of Comparison and Logical Operators**: Recap of comparison (`==`, `!=`, `<`, `>`, `<=`, `>=`) and logical operators (`and`, `or`, `not`) from Unit 1, with emphasis on `!=`, `not`, and their negations.
  - *Sample Code*:  
    ```python
    age = 20
    print(age != 18)  # True (not equal)
    print(not (age == 18))  # True (negation of equality)
    print(age >= 18 and age < 65)  # True
    print(age == 20 or age == 21)  # True
    print(not (age >= 18 and age < 65))  # False (negation of and)
    ```
  - *Exercise*: 
    1. Write a program that checks if a number is not equal to 50 and prints a message.
    2. Use `not` to negate a condition checking if a number is less than 10.

- **Boolean Data Type and Logical XOR**: Understanding `True`, `False`, boolean expressions, and the `^` operator (bitwise XOR used as logical XOR for booleans).
  - *Sample Code*:  
    ```python
    is_student = True
    has_license = False
    print(is_student ^ has_license)  # True (one is True, one is False)
    print(not (is_student ^ has_license))  # False (negation of XOR)
    print(type(is_student))  # <class 'bool'>
    ```
  - *Exercise*: 
    1. Create two boolean variables and print the result of their XOR (`^`) and its negation.
    2. Write a program that checks if exactly one of two conditions (e.g., age > 18, has_job = True) is true using `^`.

- **If, Elif, Else Statements**: Syntax, usage, and common pitfalls (e.g., indentation, colons).
  - *Sample Code*:  
    ```python
    score = 85
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    else:
        print("C or below")
    ```
  - *Exercise*: 
    1. Write a program that takes a user’s test score (0–100) and prints their letter grade (A: 90–100, B: 80–89, C: 70–79, D: 60–69, F: below 60).
    2. Create a program that uses `!=` in an `if` statement to check if a number is not zero.

- **Nested Conditionals**: Using conditionals inside other conditionals for complex logic, incorporating logical operators.
  - *Sample Code*:  
    ```python
    age = 16
    has_permit = True
    if age >= 16 and has_permit:
        print("You can drive with supervision.")
    else:
        if not has_permit:
            print("You need a permit to drive.")
        else:
            print("Too young to drive.")
    ```
  - *Exercise*: 
    1. Write a program that checks if a user is eligible to vote (age ≥ 18) and registered, using `and` in a nested conditional.
    2. Create a nested conditional that uses `not` to check if a number is not divisible by 2 or 3.

### 2. Iteration and Looping
- **Introduction to Iteration**: Defining iteration as the process of repeating actions, implemented via loops.
  - *Sample Code*:  
    ```python
    # Iteration example: Repeating a task
    for i in range(3):
        print(f"Iteration {i + 1}")
    ```
  - *Exercise*: 
    1. Write a program that uses a loop to print "Python" five times.
    2. Add a comment explaining how iteration is used in your program.

- **For Loops**: Iterating over sequences (lists, strings, ranges) and their variations.
  - *Sample Code*:  
    ```python
    # Iterating over a list
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    # Using range
    for i in range(1, 4):
        print(i)
    ```
  - *Exercise*: 
    1. Write a program that iterates over a list of colors and prints each one.
    2. Use `range` to print odd numbers from 1 to 9.

- **While Loops**: Looping based on conditions, including infinite loops and exit conditions.
  - *Sample Code*:  
    ```python
    count = 1
    while count <= 5:
        print(count)
        count += 1
    ```
  - *Exercise*: 
    1. Write a `while` loop that prints numbers from 5 to 1 in descending order.
    2. Create a program that uses a `while` loop to keep asking for input until the user enters a number not equal to zero (`!= 0`).

- **Loop Control Statements**: Using `break`, `continue`, and `else` in loops.
  - *Sample Code*:  
    ```python
    for i in range(10):
        if i == 5:
            break  # Exit loop
        if i % 2 == 0:
            continue  # Skip even numbers
        print(i)
    # Else with loop
    numbers = [1, 3, 5]
    for num in numbers:
        if num == 0:
            break
    else:
        print("No zero found.")
    ```
  - *Exercise*: 
    1. Write a loop that stops when it finds a number divisible by 6 using `break`.
    2. Use `continue` to print only numbers not equal to 3 in a range from 1 to 10.
    3. Write a loop with an `else` clause to check if a list contains a number greater than 100.

- **Nested Loops**: Loops within loops for multi-level iteration.
  - *Sample Code*:  
    ```python
    for i in range(1, 4):
        for j in range(1, 3):
            print(f"i={i}, j={j}")
    ```
  - *Exercise*: 
    1. Write a nested loop to print a 4x2 grid of dollar signs ($).
    2. Create a program that prints multiplication tables for numbers 2 to 4.

### 3. Program Flow Enhancements
- **Flags and Exit Conditions**: Using boolean flags to control program flow, incorporating `not` and `!=`.
  - *Sample Code*:  
    ```python
    found = False
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        if num != 3:
            continue
        found = True
        break
    print("Number 3 found" if found else "Number 3 not found")
    ```
  - *Exercise*: 
    1. Write a program that uses a flag to check if a user’s input is not in a list of forbidden words.
    2. Create a `while` loop that stops when a user enters a number not equal to -1, using a flag.

- **Basic Error Handling**: Using `try`/`except` to handle common errors (e.g., invalid input).
  - *Sample Code*:  
    ```python
    try:
        num = int(input("Enter a number: "))
        if num == 0:
            print("Number is zero.")
        else:
            print(f"You entered {num}")
    except ValueError:
        print("Invalid input! Please enter a number.")
    ```
  - *Exercise*: 
    1. Write a program that divides two user-input numbers, handling division by zero with `try`/`except`.
    2. Create a program that converts input to an integer and uses `!=` to check if it’s not zero, handling invalid input.

### 4. Number Systems and Bitwise Operations
- **Binary vs. Decimal Information and Bitwise XOR**: Understanding number systems and the `^` operator for bitwise operations.
  - *Sample Code*:  
    ```python
    decimal_num = 42
    binary_str = bin(decimal_num)  # Convert to binary: 0b101010
    print(binary_str)
    binary_num = 0b101010  # Binary literal
    print(binary_num)  # 42
    a = 5  # 0b0101
    b = 3  # 0b0011
    print(a ^ b)  # 6 (0b0110)
    print(not (a ^ b == 6))  # False (negation of XOR result)
    ```
  - *Exercise*: 
    1. Write a program that converts a user-entered decimal number to binary using `bin`.
    2. Use the `^` operator on two integers (e.g., 7 and 4) and print the result in binary.

### 5. Coding Best Practices
- **Coding for Others**: Writing readable code using PEP 8 guidelines, meaningful variable names, and comments.
  - *Sample Code*:  
    ```python
    # Calculate square of a number (PEP 8 compliant)
    def calculate_square(number):
        """Returns the square of the given number."""
        result = number ** 2
        return result

    user_input = int(input("Enter a number to square: "))
    squared_value = calculate_square(user_input)
    print(f"The square of {user_input} is {squared_value}")
    ```
  - *Exercise*: 
    1. Refactor a program from a previous exercise to follow PEP 8 (e.g., proper spacing, meaningful names).
    2. Write a program with comments explaining a conditional that uses `and` or `or`.

&copy; 2026 LogosTeach - All Rights Reserved