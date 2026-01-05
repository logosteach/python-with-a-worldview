## Unit 7: Testing in Python

### 1. Introduction to Testing
- **The assert Statement**: Using Python’s built-in `assert` for simple condition checks and introducing testing concepts.
  - *Sample Code*:  
    ```python
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b
    
    # Using assert for basic testing
    assert add(2, 3) == 5, "Expected 2 + 3 to equal 5"
    assert add(-1, 1) == 0, "Expected -1 + 1 to equal 0"
    print("All assertions passed!")
    # This will raise AssertionError:
    # assert add(2, 2) == 5, "This will fail"
    ```
  - *Exercise*: 
    1. Write a function `multiply` and use `assert` to test it with three input pairs.
    2. Create a program that uses `assert` to check if a string’s length is greater than 3, handling the `AssertionError` with a `try`/`except`.

- **Why Test?**: Understanding the importance of testing for reliability and maintenance, building on `assert`.
  - *Sample Code*:  
    ```python
    def divide(a, b):
        return a / b
    
    # Manual testing with assert
    try:
        assert divide(10, 2) == 5, "Division failed"
        assert divide(10, 0), "Should raise an error"
    except ZeroDivisionError:
        print("Caught division by zero!")
    except AssertionError as e:
        print(f"Test failed: {e}")
    ```
  - *Exercise*: 
    1. Write a function `is_positive` and use `assert` to test positive and negative inputs.
    2. Explain in a comment why `assert` alone is insufficient for large-scale testing.

### 2. Testing with unittest
- **Using unittest Module**: Writing test cases with `unittest`, leveraging assertion methods.
  - *Sample Code*:  
    ```python
    import unittest
    
    def add(a, b):
        return a + b
    
    class TestAddFunction(unittest.TestCase):
        def test_add_positive(self):
            self.assertEqual(add(2, 3), 5)
        
        def test_add_negative(self):
            self.assertEqual(add(-1, 1), 0)
    
    if __name__ == "__main__":
        unittest.main()
    ```
  - *Exercise*: 
    1. Write a `unittest` test case for a function that calculates the square of a number.
    2. Create a `unittest` test for a function that returns the maximum of two numbers, using `assertEqual`.

- **Setup and Teardown in unittest**: Using `setUp` and `tearDown` for test initialization and cleanup.
  - *Sample Code*:  
    ```python
    import unittest
    
    class TestStringMethods(unittest.TestCase):
        def setUp(self):
            self.test_string = "Hello"
        
        def test_upper(self):
            self.assertEqual(self.test_string.upper(), "HELLO")
        
        def test_lower(self):
            self.assertEqual(self.test_string.lower(), "hello")
        
        def tearDown(self):
            self.test_string = None
    
    if __name__ == "__main__":
        unittest.main()
    ```
  - *Exercise*: 
    1. Write a `unittest` test case with `setUp` to initialize a list and test its `append` method.
    2. Create a `unittest` test with `tearDown` to reset a variable after testing a function.

### 3. Testing with pytest
- **Using pytest**: Writing simpler tests with `pytest`, building on `assert` syntax.
  - *Sample Code*:  
    ```python
    # Save as test_math.py
    def add(a, b):
        return a + b
    
    def test_add_positive():
        assert add(2, 3) == 5
    
    def test_add_negative():
        assert add(-1, 1) == 0
    ```
    ```bash
    # Run in terminal: pytest test_math.py
    ```
  - *Exercise*: 
    1. Write a `pytest` test for a function that checks if a string is uppercase, using `assert`.
    2. Create a `pytest` test for a function that divides two numbers, testing valid and zero-division cases with `assert`.

- **Pytest Fixtures**: Using fixtures for reusable test setup.
  - *Sample Code*:  
    ```python
    import pytest
    
    @pytest.fixture
    def sample_list():
        return [1, 2, 3]
    
    def test_list_append(sample_list):
        sample_list.append(4)
        assert sample_list == [1, 2, 3, 4]
    
    def test_list_length(sample_list):
        assert len(sample_list) == 3
    ```
  - *Exercise*: 
    1. Write a `pytest` fixture that creates a dictionary and test its `get` method with `assert`.
    2. Create a `pytest` fixture for a string and test its `split` method.

### 4. Test-Driven Development (TDD)
- **TDD: What, Why, How**: Writing tests first, then code, using the red-green-refactor cycle with `assert` or framework assertions.
  - *Sample Code*:  
    ```python
    import unittest
    
    # Step 1: Write failing test (red)
    class TestCalculator(unittest.TestCase):
        def test_subtract(self):
            self.assertEqual(subtract(5, 3), 2)
    
    # Step 2: Write minimal code to pass (green)
    def subtract(a, b):
        return a - b
    
    # Step 3: Refactor if needed
    if __name__ == "__main__":
        unittest.main()
    ```
  - *Exercise*: 
    1. Use TDD to write a test for a `is_even` function using `assertEqual`, then implement it to pass.
    2. Follow TDD to create a function that checks if a number is positive, writing a `pytest` test first with `assert`.

### 5. Additional Testing Types
- **Integration Testing**: Testing interactions between components (e.g., functions, classes).
  - *Sample Code*:  
    ```python
    import unittest
    
    class Database:
        def __init__(self):
            self.data = {}
        
        def add_user(self, name, id):
            self.data[id] = name
    
    class App:
        def __init__(self):
            self.db = Database()
        
        def register_user(self, name, id):
            self.db.add_user(name, id)
            return self.db.data.get(id)
    
    class TestAppIntegration(unittest.TestCase):
        def test_register_user(self):
            app = App()
            result = app.register_user("Alice", 1)
            self.assertEqual(result, "Alice")
    
    if __name__ == "__main__":
        unittest.main()
    ```
  - *Exercise*: 
    1. Write an integration test for a class method that uses another class’s method (e.g., a `Bank` class depositing to an `Account`).
    2. Create an integration test for a function that processes data from a dictionary (Unit 1).

- **Functional Testing**: Testing functionality from a user perspective.
  - *Sample Code*:  
    ```python
    import unittest
    
    def process_order(items, discount=0):
        total = sum(items) * (1 - discount)
        return total
    
    class TestOrderProcessing(unittest.TestCase):
        def test_order_with_discount(self):
            self.assertEqual(process_order([100, 200], 0.1), 270.0)
    
    if __name__ == "__main__":
        unittest.main()
    ```
  - *Exercise*: 
    1. Write a functional test for a function that calculates a shopping cart total with tax.
    2. Create a functional test for a function that formats a user’s full name from first and last names.

- **Performance Testing (Overview)**: Introduction to testing code efficiency.
  - *Sample Code*:  
    ```python
    import time
    
    def slow_function(n):
        total = 0
        for i in range(n):
            total += i
        return total
    
    def test_performance():
        start = time.time()
        slow_function(1000000)
        elapsed = time.time() - start
        assert elapsed < 1, f"Function took too long: {elapsed} seconds"
    
    if __name__ == "__main__":
        test_performance()
    ```
  - *Exercise*: 
    1. Write a performance test that checks if a loop-based sum function runs in under 0.5 seconds for 100,000 iterations.
    2. Create a performance test for a sorting function from Unit 6 (e.g., bubble sort) with a small list.

### 6. Testing Best Practices
- **Mocking and Test Coverage**: Using mocks to isolate tests and measuring coverage.
  - *Sample Code*:  
    ```python
    import unittest
    from unittest.mock import patch
    
    def read_file(filename):
        with open(filename, "r") as file:
            return file.read()
    
    class TestFileReading(unittest.TestCase):
        @patch("builtins.open")
        def test_read_file(self, mock_open):
            mock_open.return_value.__enter__.return_value.read.return_value = "Mocked content"
            result = read_file("fake.txt")
            self.assertEqual(result, "Mocked content")
    
    if __name__ == "__main__":
        unittest.main()
    ```
    ```bash
    # For coverage: pip install coverage
    # Run: coverage run -m unittest test_file.py
    # Report: coverage report
    ```
  - *Exercise*: 
    1. Write a `unittest` test that mocks a function returning a random number and tests its output with `assertEqual`.
    2. Create a `pytest` test with a mock for a file-reading function (Unit 5) and verify its behavior with `assert`.

- **Writing Clear Tests**: Best practices for readable, maintainable tests with descriptive names and docstrings.
  - *Sample Code*:  
    ```python
    import unittest
    
    def is_positive(num):
        """Returns True if num is positive."""
        return num > 0
    
    class TestIsPositive(unittest.TestCase):
        """Tests for the is_positive function."""
        def test_positive_number(self):
            """Test that a positive number returns True."""
            self.assertTrue(is_positive(5))
        
        def test_negative_number(self):
            """Test that a negative number returns False."""
            self.assertFalse(is_positive(-5))
    
    if __name__ == "__main__":
        unittest.main()
    ```
  - *Exercise*: 
    1. Write a `unittest` test case with descriptive method names and docstrings for a string length function.
    2. Refactor a `pytest` test from a previous exercise to include a docstring and clear test names, using `assert`.
   
&copy; 2026 LogosTeach - All Rights Reserved
