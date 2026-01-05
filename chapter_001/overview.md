## Unit 1: Introduction to Python Programming

### 1. Setting Up the Python Environment
- **Installing Python**: Downloading and installing the latest version of Python from the official website.
  - *Sample Code*: No code example needed for installation, but students can verify installation by running `python --version` in the terminal/command prompt.
  - *Exercise*: 
    1. Download and install Python from python.org. Verify the installation by running `python --version` in a terminal. Write down the version number.
    2. Open a terminal and type `python` to start the Python interactive shell. Type `print("Hello, Python!")` and confirm it runs.

- **Choosing an IDE**:
  - Introduction to IDLE (Python's default IDE) and its shell/editor windows.
    - *Sample Code*: In IDLE shell:  
      ```python
      print("Hello from IDLE!")
      ```
    - *Exercise*: 
      1. Open IDLE and use the shell to print your name.
      2. Create a new file in IDLE, write `print("Welcome to Python!")`, save it as `welcome.py`, and run it.
  - Downloading and installing Visual Studio Code (VS Code) as the primary IDE for the course.
    - *Sample Code*: No code example needed for installation.
    - *Exercise*: 
      1. Download and install VS Code from code.visualstudio.com.
      2. Install the Python extension in VS Code and select the Python interpreter.
  - Configuring VS Code for Python development (installing Python extension, setting up the interpreter).
    - *Sample Code*: In VS Code terminal:  
      ```python
      print("Hello from VS Code!")
      ```
    - *Exercise*: 
      1. Create a new file in VS Code named `test.py`. Write `print("VS Code setup complete!")`, save, and run it using the "Run Python File" button.

### 2. Python Fundamentals
- **Basic Syntax**:
  - Overview of Python keywords (e.g., `if`, `for`, `while`, `def`).
    - *Sample Code*:  
      ```python
      # Keywords are reserved words
      if True:
          print("This uses the 'if' keyword.")
      ```
    - *Exercise*: 
      1. Write a program that uses the `if` keyword to print "Python is fun" if a variable `is_fun` is set to `True`.
      2. List five Python keywords not mentioned in the sample code (e.g., `else`, `while`).
  - Writing comments (`#` for single-line, `'''` for multi-line).
    - *Sample Code*:  
      ```python
      # This is a single-line comment
      '''
      This is a
      multi-line comment
      '''
      print("Comments are ignored by Python.")
      ```
    - *Exercise*: 
      1. Write a program with a single-line comment explaining what the program does and a multi-line comment describing your favorite Python feature.
      2. Add a comment to the sample code explaining why comments are useful.
  - Variables: Declaration, naming conventions, and assignment.
    - *Sample Code*:  
      ```python
      my_variable = 42  # Variable assignment
      print(my_variable)
      ```
    - *Exercise*: 
      1. Create variables for your name, age, and favorite number. Print each variable.
      2. Write a program that swaps the values of two variables (e.g., `a = 5`, `b = 10` becomes `a = 10`, `b = 5`).

- **Basic Input/Output**:
  - Using the `print` function (including escape characters: `\n`, `\t`, etc.).
    - *Sample Code*:  
      ```python
      print("Hello, World!\nThis is a new line.\tThis is tabbed.")
      ```
    - *Exercise*: 
      1. Write a program that prints a message with two new lines and a tabbed word.
      2. Use escape characters to print a quote, e.g., She said, "Hello!".
  - Using the `input` function for user input.
    - *Sample Code*:  
      ```python
      name = input("Enter your name: ")
      print("Hello, " + name + "!")
      ```
    - *Exercise*: 
      1. Write a program that asks for the user’s favorite color and prints "Your favorite color is [color]!".
      2. Create a program that asks for two numbers (as strings), adds them, and prints the result (note: you may need to convert the input).

- **Built-in Functions**: Introduction to common built-in functions (e.g., `len`, `type`, `str`).
  - *Sample Code*:  
    ```python
    my_list = [1, 2, 3]
    print(len(my_list))  # Output: 3
    print(type(my_list))  # Output: <class 'list'>
    num = 42
    print(str(num))  # Output: '42'
    ```
  - *Exercise*: 
    1. Create a string and use `len` to print its length.
    2. Write a program that uses `type` to check the data type of three different variables (e.g., a number, a string, and a list).

### 3. Data Types and Operations
- **Core Data Types**:
  - Numbers: Integers and floats (including floating-point precision).
    - *Sample Code*:  
      ```python
      integer = 10
      floating_point = 3.14159
      print(integer + floating_point)  # Output: 13.14159
      ```
    - *Exercise*: 
      1. Write a program that adds an integer and a float, then prints the result.
      2. Calculate the area of a circle with radius 5 (use 3.14 for π).
  - Strings: Creation, immutability, and basic manipulation (e.g., concatenation, slicing).
    - *Sample Code*:  
      ```python
      greeting = "Hello"
      world = "World"
      full = greeting + " " + world  # Concatenation
      print(full[0:5])  # Slicing: Output: Hello
      ```
    - *Exercise*: 
      1. Concatenate your first and last name with a space between them and print the result.
      2. Use slicing to print the first three characters of a string "Python".
  - Lists: Creation, indexing, slicing, and basic methods (e.g., `append`, `remove`).
    - *Sample Code*:  
      ```python
      fruits = ["apple", "banana", "cherry"]
      print(fruits[1])  # Indexing: Output: banana
      fruits.append("date")
      fruits.remove("banana")
      print(fruits)  # Output: ['apple', 'cherry', 'date']
      ```
    - *Exercise*: 
      1. Create a list of five favorite foods, append a new food, and remove one. Print the updated list.
      2. Use indexing to print the second and last items in a list.
  - Tuples: Creation, immutability, and use cases.
    - *Sample Code*:  
      ```python
      coordinates = (10, 20)
      print(coordinates[0])  # Output: 10
      # coordinates[0] = 15  # This would raise an error due to immutability
      ```
    - *Exercise*: 
      1. Create a tuple with three numbers and print the second number.
      2. Try to modify a tuple and explain the error you get.
  - Sets: Creation, uniqueness, and basic operations (e.g., `union`, `intersection`).
    - *Sample Code*:  
      ```python
      set_a = {1, 2, 3}
      set_b = {3, 4, 5}
      print(set_a.union(set_b))  # Output: {1, 2, 3, 4, 5}
      print(set_a.intersection(set_b))  # Output: {3}
      ```
    - *Exercise*: 
      1. Create two sets of numbers and print their union and intersection.
      2. Add a new number to a set and try adding a duplicate to confirm uniqueness.
  - Dictionaries: Creation, key-value pairs, and basic methods (e.g., `get`, `keys`).
    - *Sample Code*:  
      ```python
      person = {"name": "Alice", "age": 30}
      print(person.get("name"))  # Output: Alice
      print(person.keys())  # Output: dict_keys(['name', 'age'])
      ```
    - *Exercise*: 
      1. Create a dictionary with keys for "city" and "country" and print the value of "city".
      2. Add a new key-value pair to the dictionary and print all keys.

- **Type Casting**: Converting between data types (e.g., `int()`, `float()`, `str()`).
  - *Sample Code*:  
    ```python
    num_str = "42"
    num_int = int(num_str)
    print(num_int + 1)  # Output: 43
    ```
  - *Exercise*: 
    1. Ask the user for a number as input (string), convert it to an integer, and add 10 to it.
    2. Convert a float (e.g., 5.7) to an integer and print the result.

- **Operators**:
  - Arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`).
    - *Sample Code*:  
      ```python
      a = 10
      b = 3
      print(a + b)  # 13
      print(a / b)  # 3.333...
      print(a // b)  # 3
      print(a % b)  # 1
      print(a ** b)  # 1000
      ```
    - *Exercise*: 
      1. Write a program that calculates the remainder and quotient of 17 divided by 5.
      2. Compute 2 raised to the power of 3 and print the result.
  - Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`).
    - *Sample Code*:  
      ```python
      print(5 == 5)  # True
      print(5 != 3)  # True
      print(5 < 3)  # False
      ```
    - *Exercise*: 
      1. Write a program that checks if a user’s age (input) is greater than or equal to 18.
      2. Compare two numbers (e.g., 10 and 20) using `!=` and print the result.
  - Logical operators (`and`, `or`, `not`).
    - *Sample Code*:  
      ```python
      print(True and False)  # False
      print(True or False)  # True
      print(not True)  # False
      ```
    - *Exercise*: 
      1. Write a program that checks if a number is positive AND even.
      2. Use `or` to check if a number is either less than 0 or greater than 100.
  - Order of operations (precedence and associativity).
    - *Sample Code*:  
      ```python
      result = 2 + 3 * 4  # Multiplication first: 2 + 12 = 14
      print(result)
      ```
    - *Exercise*: 
      1. Write an expression using at least three arithmetic operators and predict the result before running it.
      2. Add parentheses to `5 + 3 * 2` to change the result and print it.

### 4. String Manipulation
- **String Methods**: Common methods (e.g., `upper`, `lower`, `strip`, `replace`).
  - *Sample Code*:  
    ```python
    text = "  Hello World  "
    print(text.upper())  # HELLO WORLD
    print(text.lower())  #   hello world  
    print(text.strip())  # Hello World
    print(text.replace("World", "Python"))  #   Hello Python  
    ```
  - *Exercise*: 
    1. Take a string with extra spaces (e.g., "  Python  ") and use `strip` to clean it, then convert it to uppercase.
    2. Replace a word in a sentence (e.g., change "cat" to "dog" in "I have a cat").

- **String Formatting**: Using f-strings for modern string interpolation.
  - *Sample Code*:  
    ```python
    name = "Bob"
    age = 25
    print(f"{name} is {age} years old.")
    ```
  - *Exercise*: 
    1. Use an f-string to print a sentence with your name and favorite hobby.
    2. Create an f-string that includes a calculated value, e.g., "The total is [5 + 3]".

- **String Operations**: Slicing, indexing, and concatenation.
  - *Sample Code*:  
    ```python
    s = "Python"
    print(s[0])  # P (indexing)
    print(s[1:4])  # yth (slicing)
    print(s + " is fun!")  # Concatenation
    ```
  - *Exercise*: 
    1. Use indexing to print the last character of a string.
    2. Slice a string to extract the middle three characters and concatenate it with another string.

&copy; 2026 LogosTeach - All Rights Reserved