## Unit 4: Object-Oriented Programming in Python

### 1. Introduction to Classes and OOP
- **Classes and Their Purpose**: Defining classes, their role in organizing code, and the basics of OOP.
  - *Sample Code*:  
    ```python
    class Dog:
        def __init__(self, name):
            self.name = name  # Instance variable
    
        def bark(self):
            return f"{self.name} says Woof!"
    
    my_dog = Dog("Buddy")
    print(my_dog.bark())  # Output: Buddy says Woof!
    ```
  - *Exercise*: 
    1. Create a `Cat` class with a `name` attribute and a `meow` method that returns "[name] says Meow!".
    2. Write a program that creates two `Dog` objects and calls their `bark` methods.

- **Instances and Instantiation**: Creating objects (instances) from classes using the constructor.
  - *Sample Code*:  
    ```python
    class Car:
        def __init__(self, model):
            self.model = model
    
    car1 = Car("Toyota")  # Instantiation
    car2 = Car("Honda")
    print(car1.model)  # Output: Toyota
    print(car2.model)  # Output: Honda
    ```
  - *Exercise*: 
    1. Create a `Student` class with a `name` attribute and instantiate two students, printing their names.
    2. Write a program that creates a `Car` object and prints its `model` attribute.

### 2. Class Components
- **Methods**: Defining instance methods and distinguishing them from regular functions.
  - *Sample Code*:  
    ```python
    class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width
        
        def area(self):
            return self.length * self.width
    
    rect = Rectangle(5, 3)
    print(rect.area())  # Output: 15
    ```
  - *Exercise*: 
    1. Add a `perimeter` method to the `Rectangle` class that returns `2 * (length + width)`.
    2. Create a `Circle` class with a `radius` attribute and a method to calculate its area (use 3.14 for π).

- **Class vs. Instance Variables**: Understanding shared (class) vs. unique (instance) attributes.
  - *Sample Code*:  
    ```python
    class Student:
        school = "High School"  # Class variable
        
        def __init__(self, name):
            self.name = name  # Instance variable
    
    student1 = Student("Alice")
    student2 = Student("Bob")
    print(student1.name, student1.school)  # Output: Alice High School
    print(student2.name, student2.school)  # Output: Bob High School
    Student.school = "Middle School"
    print(student1.school)  # Output: Middle School
    ```
  - *Exercise*: 
    1. Create a `Book` class with a class variable `library` and instance variable `title`. Print both for two book instances.
    2. Modify the class variable `library` and confirm it changes for all instances.

### 3. OOP Principles
- **Encapsulation and Abstraction**: Hiding implementation details and exposing only necessary functionality.
  - *Sample Code*:  
    ```python
    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self._balance = balance  # Protected attribute
        
        def deposit(self, amount):
            if amount > 0:
                self._balance += amount
            return self._balance
    
    account = BankAccount("Alice")
    print(account.deposit(100))  # Output: 100
    ```
  - *Exercise*: 
    1. Create a `Person` class with a protected `_age` attribute and a method to increment age, ensuring it’s positive.
    2. Write a program that tries to access a protected attribute directly and explain the convention.

- **Inheritance**: Creating subclasses that inherit attributes and methods from a parent class.
  - *Sample Code*:  
    ```python
    class Animal:
        def __init__(self, name):
            self.name = name
        
        def speak(self):
            return "I make a sound!"
    
    class Cat(Animal):
        def speak(self):
            return f"{self.name} says Meow!"
    
    cat = Cat("Whiskers")
    print(cat.speak())  # Output: Whiskers says Meow!
    ```
  - *Exercise*: 
    1. Create a `Dog` class that inherits from `Animal` and overrides `speak` to return "[name] says Woof!".
    2. Write a program with a parent class `Vehicle` and a subclass `Bike` that adds a specific method (e.g., `pedal`).

- **Polymorphism**: Using the same method name in different classes with different behaviors.
  - *Sample Code*:  
    ```python
    class Bird:
        def speak(self):
            return "Chirp!"
    
    class Dog:
        def speak(self):
            return "Woof!"
    
    animals = [Bird(), Dog()]
    for animal in animals:
        print(animal.speak())  # Output: Chirp!, Woof!
    ```
  - *Exercise*: 
    1. Create a `Fish` class with a `speak` method and add it to a list with `Bird` and `Dog` to demonstrate polymorphism.
    2. Write a program with two classes that share a method name but implement it differently.

- **Class Composition**: Using objects of one class as attributes in another class.
  - *Sample Code*:  
    ```python
    class Engine:
        def __init__(self, horsepower):
            self.horsepower = horsepower
        
        def start(self):
            return "Engine starts!"
    
    class Car:
        def __init__(self, model, horsepower):
            self.model = model
            self.engine = Engine(horsepower)
    
    my_car = Car("Toyota", 200)
    print(my_car.engine.start())  # Output: Engine starts!
    ```
  - *Exercise*: 
    1. Create a `Person` class with a `Wallet` object as an attribute, where `Wallet` has a `balance` and `add_money` method.
    2. Write a program with a `House` class that contains a `Room` object with its own attributes and methods.

### 4. Advanced Class Features
- **Setter and Getter Methods with @property**: Controlling attribute access using properties.
  - *Sample Code*:  
    ```python
    class Person:
        def __init__(self, name):
            self._name = name
        
        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, value):
            if not value:
                raise ValueError("Name cannot be empty")
            self._name = value
    
    person = Person("Alice")
    print(person.name)  # Output: Alice
    person.name = "Bob"
    print(person.name)  # Output: Bob
    ```
  - *Exercise*: 
    1. Create a `Student` class with a `grade` property that ensures the grade is between 0 and 100.
    2. Write a program with a `name` property that converts the input to title case before storing.

- **Static Methods and Attributes**: Methods and attributes that belong to the class, not instances.
  - *Sample Code*:  
    ```python
    class MathUtils:
        pi = 3.14159  # Static attribute
        
        @staticmethod
        def square(num):
            return num * num
    
    print(MathUtils.pi)  # Output: 3.14159
    print(MathUtils.square(5))  # Output: 25
    ```
  - *Exercise*: 
    1. Create a `Converter` class with a static method to convert Celsius to Fahrenheit.
    2. Add a static attribute `max_attempts` to a `Game` class and print it.

- **Special Methods (Dunder Methods)**: Customizing object behavior with methods like `__str__`.
  - *Sample Code*:  
    ```python
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author
        
        def __str__(self):
            return f"{self.title} by {self.author}"
    
    book = Book("Python 101", "John Doe")
    print(book)  # Output: Python 101 by John Doe
    ```
  - *Exercise*: 
    1. Add a `__str__` method to a `Car` class that returns "[model] with [horsepower] HP".
    2. Create a class with a `__str__` method that formats its attributes in a custom way.

### 5. Class Design and Best Practices
- **Designing Classes and Error Handling**: Writing clear, robust classes with meaningful names, docstrings, and error handling.
  - *Sample Code*:  
    ```python
    class Temperature:
        """Class to manage temperature in Celsius."""
        def __init__(self, celsius):
            if not isinstance(celsius, (int, float)):
                raise TypeError("Temperature must be a number")
            self._celsius = celsius
        
        def to_fahrenheit(self):
            """Converts Celsius to Fahrenheit."""
            return (self._celsius * 9/5) + 32
    
    try:
        temp = Temperature(25)
        print(temp.to_fahrenheit())  # Output: 77.0
    except TypeError as e:
        print(e)
    ```
  - *Exercise*: 
    1. Create a `BankAccount` class with a docstring and a method that raises an error for negative deposits.
    2. Refactor a class from a previous exercise to include a docstring and better attribute names.
