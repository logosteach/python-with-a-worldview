
# Python Tuples – Quick Guide

## 1. Creating Tuples

```python
# Different ways to create tuples
t1 = (1, 2, 3)                    # Most common way
t2 = 10, 20, 30                   # Tuple packing (parentheses optional)
t3 = (42,)                        # Single-element tuple (comma is REQUIRED!)
t4 = tuple([5, 6, 7])             # From a list
t5 = ()                           # Empty tuple
t6 = "hello",                     # Single string tuple

print(t1)      # (1, 2, 3)
print(t3)      # (42,)
print(type(t3)) # <class 'tuple'>
```

## 2. Indexing & Accessing Values (same syntax as lists)

```python
point = (10, 25, -3)

print(point[0])      # 10
print(point[1])      # 25
print(point[-1])     # -3   (last element)
print(point[1:])     # (25, -3)   slicing returns a new tuple

# Very common: tuple unpacking
x, y, z = point
print(x, y, z)       # 10 25 -3
```

## 3. Tuple Immutability vs List Mutability

**This is the key difference:**

```python
# Tuple – IMMUTABLE
t = (1, 2, 3)
# t[1] = 99           # TypeError: 'tuple' object does not support item assignment

# You CANNOT do any of these:
# t.append(4)
# t.pop()
# t[0] = 100
# del t[1]

# List – MUTABLE
lst = [1, 2, 3]
lst[1] = 99         # ✓ Works
lst.append(4)       # ✓ Works
lst.pop()           # ✓ Works
lst[0] = 100        # ✓ Works

print(lst)          # [100, 99, 3]
```

### Side-by-side comparison example

```python
coordinates = (10, 20)     # tuple
values = [10, 20]          # list

# This works with list
values[0] = 99
values.append(30)
print("List after changes:", values)      # [99, 20, 30]

# These FAIL with tuple
# coordinates[0] = 99       # ← TypeError!
# coordinates.append(30)    # ← AttributeError!

# But reassigning the whole variable is fine (creates new tuple)
coordinates = (99, 20)
print("New coordinates:", coordinates)    # (99, 20)
```

## Quick Summary Table

| Feature                    | Tuple              | List               |
|----------------------------|--------------------|--------------------|
| Syntax                     | `(1, 2, 3)` or `1,2,3` | `[1, 2, 3]`       |
| Mutable?                   | No ✗               | Yes ✓             |
| Can change elements?       | No                 | Yes               |
| Can append/pop?            | No                 | Yes               |
| Can be used as dict key?   | Yes                | No                |
| Typical use case           | Fixed data, coordinates, return values | Dynamic collections |

**Bottom line**  
Use **tuples** when the data **should not change** (coordinates, RGB colors, days of the week, database rows, multiple return values).  
Use **lists** when you need to **modify, add, or remove** elements.