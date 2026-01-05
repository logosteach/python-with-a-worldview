## Unit 9: Building GUIs with Tkinter and Pillow

### 1. Introduction to Tkinter
- **Setting Up Tkinter**: Verifying Tkinter installation and creating a basic window.
  - *Sample Code*:  
    ```python
    import tkinter as tk
    
    # Create a basic window
    window = tk.Tk()
    window.title("My First GUI")
    window.geometry("300x200")  # Width x Height
    window.mainloop()
    ```
  - *Exercise*: 
    1. Create a Tkinter window with the title "Hello GUI" and size 400x300.
    2. Add a comment explaining the role of `mainloop()` in the program.

- **Common Tkinter Widgets**: Using `Label`, `Button`, `Entry`, and `Canvas` widgets.
  - *Sample Code*:  
    ```python
    import tkinter as tk
    
    window = tk.Tk()
    window.title("Widgets Demo")
    
    # Label
    label = tk.Label(window, text="Enter your name:")
    label.pack()
    
    # Entry
    entry = tk.Entry(window)
    entry.pack()
    
    # Button
    button = tk.Button(window, text="Click Me")
    button.pack()
    
    window.mainloop()
    ```
  - *Exercise*: 
    1. Create a Tkinter window with a `Label` displaying "Welcome" and an `Entry` for user input.
    2. Add a `Button` labeled "Submit" to the window and test the layout.

### 2. Tkinter Layout and Event Handling
- **Geometry Managers**: Using `pack`, `grid`, and `place` for widget layout.
  - *Sample Code*:  
    ```python
    import tkinter as tk
    
    window = tk.Tk()
    window.title("Layout Demo")
    
    # Grid layout
    label = tk.Label(window, text="Name:")
    label.grid(row=0, column=0)
    
    entry = tk.Entry(window)
    entry.grid(row=0, column=1)
    
    button = tk.Button(window, text="Submit")
    button.grid(row=1, column=0, columnspan=2)
    
    window.mainloop()
    ```
  - *Exercise*: 
    1. Create a window with two `Entry` widgets and a `Button` using `grid` layout in a 2x2 arrangement.
    2. Use `pack` to stack three `Label` widgets vertically in a window.

- **Event-Driven Programming**: Binding events (e.g., button clicks, mouse events) to functions.
  - *Sample Code*:  
    ```python
    import tkinter as tk
    
    def on_button_click():
        label.config(text="Button Clicked!")
    
    window = tk.Tk()
    window.title("Event Demo")
    
    label = tk.Label(window, text="Click the button")
    label.pack()
    
    button = tk.Button(window, text="Click Me", command=on_button_click)
    button.pack()
    
    window.mainloop()
    ```
  - *Exercise*: 
    1. Create a button that changes a label’s text to "Hello!" when clicked.
    2. Write a program that binds a keypress event (e.g., Enter key) to print a message to the console.

### 3. Data Handling and Error Checking
- **Handling User Input**: Retrieving and processing data from `Entry` widgets.
  - *Sample Code*:  
    ```python
    import tkinter as tk
    
    def submit():
        name = entry.get()
        label.config(text=f"Hello, {name}!")
    
    window = tk.Tk()
    window.title("Input Demo")
    
    entry = tk.Entry(window)
    entry.pack()
    
    button = tk.Button(window, text="Submit", command=submit)
    button.pack()
    
    label = tk.Label(window, text="Enter your name")
    label.pack()
    
    window.mainloop()
    ```
  - *Exercise*: 
    1. Create a window with an `Entry` widget that displays the entered text in a `Label` when a button is clicked.
    2. Write a program that takes two numbers from `Entry` widgets and displays their sum in a `Label`.

- **Error Checking Input**: Validating user input with `try`/`except` (Units 2, 5).
  - *Sample Code*:  
    ```python
    import tkinter as tk
    
    def calculate():
        try:
            num = int(entry.get())
            label.config(text=f"Double: {num * 2}")
        except ValueError:
            label.config(text="Error: Enter a valid number")
    
    window = tk.Tk()
    window.title("Error Checking")
    
    entry = tk.Entry(window)
    entry.pack()
    
    button = tk.Button(window, text="Calculate", command=calculate)
    button.pack()
    
    label = tk.Label(window, text="Enter a number")
    label.pack()
    
    window.mainloop()
    ```
  - *Exercise*: 
    1. Create a window that validates an `Entry` input as a positive integer and displays an error if invalid.
    2. Write a program that checks if an `Entry` input is a non-empty string before updating a `Label`.

### 4. Building an MSPaint Clone with Tkinter and Pillow
- **Introduction to Pillow**: Installing (`pip install Pillow`) and basic image operations (creating, saving images).
  - *Sample Code*:  
    ```python
    from PIL import Image, ImageDraw
    
    # Create and save an image
    image = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((50, 50, 150, 150), fill="blue")
    image.save("sample.png")
    ```
  - *Exercise*: 
    1. Install Pillow and create a 300x300 image with a red circle; save it as `circle.png`.
    2. Write a program that creates a white 200x200 image with a green line and saves it.

- **MSPaint Clone Project**: Building a simple drawing app with Tkinter’s `Canvas` and Pillow for saving drawings.
  - *Sample Code*:  
    ```python
    import tkinter as tk
    from PIL import Image, ImageDraw
    import os
    
    class MSPaintClone:
        def __init__(self, root):
            self.root = root
            self.root.title("MSPaint Clone")
            
            # Canvas for drawing
            self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
            self.canvas.pack(pady=10)
            
            # Bind mouse events
            self.canvas.bind("<B1-Motion>", self.draw)
            self.last_x, self.last_y = None, None
            
            # Save button
            self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
            self.save_button.pack()
            
            # Initialize Pillow image
            self.image = Image.new("RGB", (400, 300), "white")
            self.draw_image = ImageDraw.Draw(self.image)
        
        def draw(self, event):
            x, y = event.x, event.y
            if self.last_x and self.last_y:
                self.canvas.create_line(self.last_x, self.last_y, x, y, fill="black", width=2)
                self.draw_image.line((self.last_x, self.last_y, x, y), fill="black", width=2)
            self.last_x, self.last_y = x, y
        
        def save_image(self):
            try:
                self.image.save("drawing.png")
                self.canvas.create_text(200, 20, text="Saved as drawing.png", fill="green")
            except Exception as e:
                self.canvas.create_text(200, 20, text=f"Error: {e}", fill="red")
    
    window = tk.Tk()
    app = MSPaintClone(window)
    window.mainloop()
    ```
  - *Exercise*: 
    1. Modify the MSPaint clone to add a button that changes the drawing color to red.
    2. Extend the MSPaint clone to allow drawing rectangles on the canvas with a button toggle.

## Teaching Sequence Rationale
1. **Tkinter Basics First**: Setting up a window and introducing widgets builds on Units 1–3’s syntax and functions.
2. **Layout and Event Handling**: Geometry managers and event binding enable interactive GUIs, using Unit 4’s OOP for structure.
3. **Data Handling and Error Checking**: Input processing and validation leverage Units 1, 2, and 5’s concepts for robust applications.
4. **MSPaint Clone with Pillow**: Combines Tkinter’s `Canvas`, Pillow’s image processing, and prior units’ skills (OOP, error handling) in a practical project.

## Notes
- **Installation**: Tkinter is included with Python; Pillow requires `pip install Pillow`.
- **Beginner Focus**: Examples use simple widgets and basic drawing to avoid complexity.
- **MSPaint Clone**: Simplified to freehand drawing and saving, with options to extend (e.g., colors, shapes).
- **Overlap Handling**: Functions (Unit 3), classes (Unit 4), and error handling (Units 2, 5) are applied to GUI contexts without redundancy.
- **Exercises**: Encourage testing with Unit 7’s tools (e.g., `pytest` for input validation functions) and connect to prior units (e.g., data types, loops).
- **No Operator Overlap**: Unit 2’s operators (`!=`, `not`, `and`, `or`, `^`) are used in validation but not reintroduced.

&copy; 2026 LogosTeach - All Rights Reserved
