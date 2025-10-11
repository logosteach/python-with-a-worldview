## Unit 6: Algorithms and Data Structures in Python

### 1. Introduction to Algorithm Analysis
- **Big O Notation**: Understanding time and space complexity to evaluate algorithm efficiency.
  - *Sample Code*:  
    ```python
    def linear_example(n):
        """O(n) complexity: loops through n items."""
        for i in range(n):
            print(i)
    
    def constant_example():
        """O(1) complexity: single operation."""
        return 42
    
    print("Linear example:")
    linear_example(5)
    print("Constant example:", constant_example())
    ```
  - *Exercise*: 
    1. Write a function with O(1) complexity that returns the first element of a list.
    2. Create a function with O(n) complexity that prints each element of a list and explain its complexity in a comment.

### 2. Search Algorithms
- **Linear Search**: Sequentially checking each element to find a target.
  - *Sample Code*:  
    ```python
    def linear_search(arr, target):
        """Finds index of target in arr using linear search, O(n)."""
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
    
    numbers = [4, 2, 7, 1, 9]
    print(linear_search(numbers, 7))  # Output: 2
    print(linear_search(numbers, 5))  # Output: -1
    ```
  - *Exercise*: 
    1. Write a linear search function that returns `True` if a target string is in a list.
    2. Create a program that uses linear search to find the first even number in a list.

- **Binary Search**: Efficiently searching a sorted list by dividing the search space.
  - *Sample Code*:  
    ```python
    def binary_search(arr, target):
        """Finds index of target in sorted arr using binary search, O(log n)."""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    sorted_numbers = [1, 3, 5, 7, 9]
    print(binary_search(sorted_numbers, 5))  # Output: 2
    print(binary_search(sorted_numbers, 6))  # Output: -1
    ```
  - *Exercise*: 
    1. Write a recursive binary search function and test it on a sorted list.
    2. Create a program that sorts a list (using `sorted`) and uses binary search to find a user-input number.

- **Interpolation Search**: Improving Binary Search for uniformly distributed data.
  - *Sample Code*:  
    ```python
    def interpolation_search(arr, target):
        """Finds index of target in sorted arr, O(log log n) for uniform data."""
        left, right = 0, len(arr) - 1
        while left <= right and arr[left] <= target <= arr[right]:
            # Estimate position based on uniform distribution
            pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
            if pos < left or pos > right:
                return -1
            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                left = pos + 1
            else:
                right = pos - 1
        return -1
    
    uniform_numbers = [10, 20, 30, 40, 50]
    print(interpolation_search(uniform_numbers, 30))  # Output: 2
    ```
  - *Exercise*: 
    1. Write a program that uses interpolation search to find a number in a sorted list of multiples of 10.
    2. Compare interpolation search with binary search on a sorted list and print their results.

### 3. Sorting Algorithms
- **Bubble Sort**: Repeatedly swapping adjacent elements to sort a list.
  - *Sample Code*:  
    ```python
    def bubble_sort(arr):
        """Sorts arr using bubble sort, O(n^2)."""
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    numbers = [64, 34, 25, 12, 22]
    print(bubble_sort(numbers))  # Output: [12, 22, 25, 34, 64]
    ```
  - *Exercise*: 
    1. Write a bubble sort function that sorts a list of strings alphabetically.
    2. Modify bubble sort to count and print the number of swaps performed.

- **Selection Sort**: Repeatedly selecting the smallest element to build a sorted list.
  - *Sample Code*:  
    ```python
    def selection_sort(arr):
        """Sorts arr using selection sort, O(n^2)."""
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    
    numbers = [64, 34, 25, 12, 22]
    print(selection_sort(numbers))  # Output: [12, 22, 25, 34, 64]
    ```
  - *Exercise*: 
    1. Write a selection sort function that sorts a list in descending order.
    2. Create a program that uses selection sort and prints the list after each iteration.

- **Insertion Sort**: Building a sorted list by inserting elements in the correct position.
  - *Sample Code*:  
    ```python
    def insertion_sort(arr):
        """Sorts arr using insertion sort, O(n^2)."""
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    numbers = [64, 34, 25, 12, 22]
    print(insertion_sort(numbers))  # Output: [12, 22, 25, 34, 64]
    ```
  - *Exercise*: 
    1. Write an insertion sort function that sorts a list of floating-point numbers.
    2. Create a program that uses insertion sort and prints the list after each insertion.

- **Quick Sort**: Dividing the list around a pivot to sort recursively.
  - *Sample Code*:  
    ```python
    def quick_sort(arr):
        """Sorts arr using quick sort, average O(n log n)."""
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
    numbers = [64, 34, 25, 12, 22]
    print(quick_sort(numbers))  # Output: [12, 22, 25, 34, 64]
    ```
  - *Exercise*: 
    1. Write a quick sort function that uses the first element as the pivot.
    2. Create a program that applies quick sort and prints the pivot at each recursive step.

- **Merge Sort**: Dividing and merging sorted sublists recursively.
  - *Sample Code*:  
    ```python
    def merge_sort(arr):
        """Sorts arr using merge sort, O(n log n)."""
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    numbers = [64, 34, 25, 12, 22]
    print(merge_sort(numbers))  # Output: [12, 22, 25, 34, 64]
    ```
  - *Exercise*: 
    1. Write a merge sort function that sorts a list of strings.
    2. Create a program that prints the left and right sublists during each merge step.

### 4. Data Structures: Stacks and Queues with Deque
- **Stacks**: Implementing a Last-In-First-Out (LIFO) structure by inheriting from `collections.deque`.
  - *Sample Code*:  
    ```python
    from collections import deque
    
    class Stack(deque):
        """A stack implementation inheriting from deque, O(1) push/pop."""
        def push(self, item):
            """Add item to the top of the stack."""
            self.append(item)
        
        def pop(self):
            """Remove and return the top item."""
            if not self:
                raise IndexError("Pop from empty stack")
            return super().pop()
        
        def is_empty(self):
            """Check if the stack is empty."""
            return len(self) == 0
    
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())  # Output: 2
    print(stack.pop())  # Output: 1
    ```
  - *Exercise*: 
    1. Create a `Stack` class that inherits from `deque` and pushes three numbers, then pops them in reverse order.
    2. Add a `peek` method to the `Stack` class to return the top item without removing it.

- **Queues**: Implementing a First-In-First-Out (FIFO) structure by inheriting from `collections.deque`.
  - *Sample Code*:  
    ```python
    from collections import deque
    
    class Queue(deque):
        """A queue implementation inheriting from deque, O(1) enqueue/dequeue."""
        def enqueue(self, item):
            """Add item to the end of the queue."""
            self.append(item)
        
        def dequeue(self):
            """Remove and return the front item."""
            if not self:
                raise IndexError("Dequeue from empty queue")
            return super().popleft()
        
        def is_empty(self):
            """Check if the queue is empty."""
            return len(self) == 0
    
    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    print(queue.dequeue())  # Output: A
    print(queue.dequeue())  # Output: B
    ```
  - *Exercise*: 
    1. Create a `Queue` class that inherits from `deque`, enqueues three names, and dequeues them in order.
    2. Add a `front` method to the `Queue` class to return the first item without removing it.

### 5. Algorithm and Data Structure Best Practices
- **Clear and Robust Implementations**: Writing efficient, readable algorithms and data structures with error handling and docstrings.
  - *Sample Code*:  
    ```python
    from collections import deque
    
    class SafeStack(deque):
        """A robust stack implementation with error handling, O(1) push/pop."""
        def push(self, item):
            """Add item to the top of the stack."""
            if item is None:
                raise ValueError("Cannot push None to stack")
            self.append(item)
        
        def pop(self):
            """Remove and return the top item."""
            if not self:
                raise IndexError("Pop from empty stack")
            return super().pop()
    
    try:
        stack = SafeStack()
        stack.push(1)
        print(stack.pop())  # Output: 1
        stack.push(None)  # Raises ValueError
    except ValueError as e:
        print(e)
    ```
  - *Exercise*: 
    1. Refactor a sorting function (e.g., bubble sort) to include a docstring and error handling for empty lists.
    2. Modify the `Queue` class to raise a custom error if enqueuing an invalid item (e.g., empty string).

&copy; 2025 LogosTeach - All Rights Reserved
