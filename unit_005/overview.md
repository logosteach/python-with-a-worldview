## Unit 5: File Handling and JSON in Python

### 1. File Handling Basics
- **File Operations (Traditional)**: Creating, opening, reading, writing, appending, and closing files using built-in functions and file modes.
  - *Sample Code*:  
    ```python
    # Writing to a file
    file = open("example.txt", "w")
    file.write("Hello, World!\n")
    file.close()
    
    # Appending to a file
    file = open("example.txt", "a")
    file.write("Another line.\n")
    file.close()
    
    # Reading from a file
    file = open("example.txt", "r")
    content = file.read()
    print(content)  # Output: Hello, World!\nAnother line.\n
    file.close()
    ```
  - *Exercise*: 
    1. Write a program that creates a file `notes.txt`, writes your name to it, and closes it.
    2. Create a program that reads `notes.txt` and prints its contents.
    3. Append a new line to `notes.txt` with today’s date and print the updated file.

- **Context Managers (`with` Statement)**: Using `with` for safe file handling to automatically close files.
  - *Sample Code*:  
    ```python
    # Writing with context manager
    with open("example.txt", "w") as file:
        file.write("Using with statement.\n")
    
    # Reading with context manager
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)  # Output: Using with statement.\n
    ```
  - *Exercise*: 
    1. Rewrite the first exercise from “File Operations” using a `with` statement.
    2. Write a program that appends a user’s input to a file using a `with` statement and reads it back.

### 2. The Pathlib Module
- **Introduction to Path Class**: Using `pathlib.Path` for modern file and directory handling.
  - *Sample Code*:  
    ```python
    from pathlib import Path
    
    # Create a Path object
    path = Path("example.txt")
    
    # Write to a file
    path.write_text("Hello from Pathlib!\n")
    
    # Read from a file
    content = path.read_text()
    print(content)  # Output: Hello from Pathlib!\n
    ```
  - *Exercise*: 
    1. Create a program that uses `Path` to write a greeting to a file named `greeting.txt`.
    2. Write a program that reads and prints the contents of `greeting.txt` using `Path`.

- **Path Class Methods**: Common methods like `exists`, `is_file`, `unlink`, and `parent`.
  - *Sample Code*:  
    ```python
    from pathlib import Path
    
    path = Path("example.txt")
    
    # Check if file exists
    print(path.exists())  # Output: True
    print(path.is_file())  # Output: True
    
    # Get parent directory
    print(path.parent)  # Output: .
    
    # Delete file
    if path.exists():
        path.unlink()
        print("File deleted")
    ```
  - *Exercise*: 
    1. Write a program that checks if a file `data.txt` exists and prints a message if it does.
    2. Create a program that deletes a file `temp.txt` if it exists, using `Path.unlink`.

### 3. Advanced Error Handling
- **Try/Except/Else/Finally Blocks**: Handling file-related errors with specific exceptions and full try-except structure.
  - *Sample Code*:  
    ```python
    try:
        with open("nonexistent.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found!")
    else:
        print("File read successfully:", content)
    finally:
        print("Execution complete.")
    ```
  - *Exercise*: 
    1. Write a program that attempts to read a file and handles `FileNotFoundError` with a custom message.
    2. Create a program that writes to a file, uses `else` to confirm success, and `finally` to print a completion message.

- **Specific File-Related Exceptions**: Handling `PermissionError`, `IsADirectoryError`, etc.
  - *Sample Code*:  
    ```python
    from pathlib import Path
    
    path = Path("protected.txt")
    try:
        path.write_text("Trying to write")
    except PermissionError:
        print("Permission denied!")
    except IsADirectoryError:
        print("That's a directory, not a file!")
    ```
  - *Exercise*: 
    1. Write a program that tries to write to a file and handles `PermissionError`.
    2. Create a program that attempts to read a directory as a file and handles `IsADirectoryError`.

### 4. JSON Data Processing
- **Working with JSON**: Serializing and deserializing data using `json.dump`, `json.load`, and related functions.
  - *Sample Code*:  
    ```python
    import json
    
    # Serialize to JSON
    data = {"name": "Alice", "age": 30}
    with open("data.json", "w") as file:
        json.dump(data, file)
    
    # Deserialize from JSON
    with open("data.json", "r") as file:
        loaded_data = json.load(file)
        print(loaded_data)  # Output: {'name': 'Alice', 'age': 30}
    ```
  - *Exercise*: 
    1. Write a program that saves a dictionary with your name and favorite color to a JSON file.
    2. Create a program that reads a JSON file and prints one of its values (e.g., the "name" key).

- **JSON with Pathlib**: Combining JSON operations with `Path` for modern file handling.
  - *Sample Code*:  
    ```python
    from pathlib import Path
    import json
    
    path = Path("data.json")
    
    # Write JSON
    data = {"city": "New York", "population": 8000000}
    path.write_text(json.dumps(data))
    
    # Read JSON
    loaded_data = json.loads(path.read_text())
    print(loaded_data["city"])  # Output: New York
    ```
  - *Exercise*: 
    1. Use `Path` to write a dictionary to a JSON file and read it back.
    2. Create a program that updates a JSON file by adding a new key-value pair using `Path`.

### 5. File Handling Best Practices
- **Clear and Robust File Operations**: Writing maintainable file-handling code with context managers, error handling, and clear naming.
  - *Sample Code*:  
    ```python
    from pathlib import Path
    
    def save_note(note, filename="note.txt"):
        """Saves a note to a file, handling errors."""
        path = Path(filename)
        try:
            path.write_text(note)
            return True
        except PermissionError:
            print("Cannot write to file: Permission denied")
            return False
    
    note = "This is a note."
    if save_note(note):
        print(f"Note saved to {Path('note.txt').absolute()}")
    ```
  - *Exercise*: 
    1. Write a function that saves user input to a file, handles errors, and uses a `Path` object.
    2. Refactor a previous file-handling program to include a docstring and meaningful variable names.

&copy; 2025 LogosTeach - All Rights Reserved
