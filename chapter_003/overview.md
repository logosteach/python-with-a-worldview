## Unit 3: Functions in Python

### 1. Introduction to Functions
- **Defining Functions**: Structure of a function (`def`, parameters, body, `return`, `pass`).
  - *Sample Code*:  
    ```python
    def greet(name):
        """Prints a greeting for the given name."""
        return f"Hello, {name}!"
    
    print(greet("Alice"))  # Output: Hello, Alice!
    
    # Using pass for an empty function
    def placeholder():
        pass
    ```
  - *Exercise*: 
    1. Write a function `say_hello` that takes no parameters and returns "Hello, World!".
    2. Create an empty function `do_nothing` using `pass` and call it.

- **Return Statements**: Using `return` to output values from functions and understanding implicit `None`.
  - *Sample Code*:  
    ```python
    def add(a, b):
        return a + b
    
    result = add(3, 4)
    print(result)  # Output: 7
    
    def no_return():
        print("No return statement")
    
    print(no_return())  # Output: No return statement, None
    ```
  - *Exercise*: 
    1. Write a function `multiply` that takes two numbers and returns their product.
    2. Create a function that prints a message but returns `None`, and print its return value to confirm.

### 2. Function Parameters
- **Arguments vs. Parameters**: Understanding parameters (in function definition) vs. arguments (values passed when calling).
  - *Sample Code*:  
    ```python
    def introduce(name, age):  # name, age are parameters
        return f"{name} is {age} years old."
    
    print(introduce("Bob", 25))  # "Bob", 25 are arguments
    ```
  - *Exercise*: 
    1. Write a function `describe_pet` with parameters `pet_name` and `pet_type`, and call it with different arguments.
    2. Explain in a comment the difference between a parameter and an argument in your code.

- **Types of Parameters**: Positional, default, and variable arguments (`*args`, `**kwargs`).
  - *Sample Code*:  
    ```python
    # Positional parameters
    def subtract(a, b):
        return a - b
    
    # Default parameters
    def greet_user(name="Guest"):
        return f"Welcome, {name}!"
    
    # Variable arguments
    def sum_numbers(*args):
        return sum(args)
    
    # Keyword arguments
    def describe_person(**kwargs):
        return kwargs
    
    print(subtract(10, 3))  # 7
    print(greet_user())  # Welcome, Guest!
    print(greet_user("Alice"))  # Welcome, Alice!
    print(sum_numbers(1, 2, 3, 4))  # 10
    print(describe_person(name="Bob", age=30))  # {'name': 'Bob', 'age': 30}
    ```
  - *Exercise*: 
    1. Write a function `calculate_total` with a default parameter for tax rate (e.g., 0.1) to compute price + tax.
    2. Create a function `print_names` that uses `*args` to print a variable number of names.
    3. Write a function `create_profile` that uses `**kwargs` to print a dictionary of user attributes.

### 3. Function Composition and Scope
- **Function Composition**: Calling one function from another to build modular programs.
  - *Sample Code*:  
    ```python
    def square(num):
        return num * num
    
    def add_squares(a, b):
        return square(a) + square(b)
    
    print(add_squares(2, 3))  # Output: 13 (4 + 9)
    ```
  - *Exercise*: 
    1. Write a function `cube` that returns a number cubed, and another function that adds two cubed numbers using `cube`.
    2. Create a function that calls another function to double a number and then adds 10 to the result.

- **Scope and Lifetime of Variables**: Local vs. global scope in functions.
  - *Sample Code*:  
    ```python
    global_var = 10
    
    def modify_local():
        local_var = 5
        print(f"Local: {local_var}, Global: {global_var}")
    
    modify_local()  # Output: Local: 5, Global: 10
    print(global_var)  # Output: 10
    # print(local_var)  # Error: local_var is not defined
    ```
  - *Exercise*: 
    1. Write a function that defines a local variable and tries to access it outside (note the error).
    2. Create a program with a global variable `count` and a function that increments it (using `global` keyword).

### 4. Advanced Function Concepts
- **Recursion**: Functions that call themselves to solve problems.
  - *Sample Code*:  
    ```python
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    
    print(factorial(5))  # Output: 120
    ```
  - *Exercise*: 
    1. Write a recursive function to calculate the sum of numbers from 1 to n.
    2. Create a recursive function to compute the nth Fibonacci number (e.g., 0, 1, 1, 2, 3, 5, ...).

- **Lambda Functions**: Anonymous functions for concise operations, often used with `map` or `filter`.
  - *Sample Code*:  
    ```python
    # Lambda for squaring
    square = lambda x: x * x
    print(square(4))  # Output: 16
    
    # Using lambda with map
    numbers = [1, 2, 3]
    squared = list(map(lambda x: x ** 2, numbers))
    print(squared)  # Output: [1, 4, 9]
    ```
  - *Exercise*: 
    1. Write a lambda function to triple a number and test it.
    2. Use a lambda with `map` to convert a list of strings to uppercase.

### 5. Function Best Practices
- **Code Clarity and Refactoring**: Writing clear functions with docstrings, meaningful names, and refactoring for simplicity.
  - *Sample Code*:  
    ```python
    # Before refactoring
    def calc(a, b):
        x = a + b
        y = x * 2
        return y
    
    # After refactoring
    def calculate_total_price(item_price, tax_rate):
        """Calculates total price including tax."""
        subtotal = item_price + (item_price * tax_rate)
        return round(subtotal, 2)
    
    print(calculate_total_price(100, 0.1))  # Output: 110.0
    ```
  - *Exercise*: 
    1. Refactor a function from a previous exercise to include a docstring and better variable names.
    2. Write a function with a docstring that takes a list and returns its maximum value.

- **Error Handling in Functions**: Validating parameters with `try`/`except` to ensure robust functions.
  - *Sample Code*:  
    ```python
    def divide_numbers(a, b):
        """Divides a by b, handling division by zero."""
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    
    print(divide_numbers(10, 2))  # Output: 5.0
    print(divide_numbers(10, 0))  # Output: Error: Division by zero is not allowed.
    ```
  - *Exercise*: 
    1. Write a function that takes a string and converts it to an integer, handling invalid inputs.
    2. Create a function that checks if a parameter is positive, raising an error if not (use `raise ValueError`).

&copy; 2026 LogosTeach - All Rights Reserved