# =============================================================================
# Practice: Data Types and Type Conversion
# Unit 2  ·  Lessons 3 and 7  ·  Foundational Elements
# =============================================================================
# Learning Objectives:
#   - Identify the four basic types used in this unit: int, float, str, bool.
#   - Use type() to check the type of a value or a variable.
#   - Explain why "7" is not the same as 7.
#   - Predict what happens when two values of the same type are combined,
#     and what happens when mixed types meet.
#   - Convert values with int(), float(), str(), and bool().
#   - Name the two common conversion errors: TypeError and ValueError.
#   - Convert a decimal-looking string in two steps when int() cannot
#     finish the work alone.
#
# Biblical Connection:
#   Lesson 3 — Different values need different handling. Jesus knew how to
#   speak to Nicodemus (John 3), the Samaritan woman (John 4), and the
#   rich young ruler (Matthew 19). He is the light that exposes darkness
#   and leads people to Himself.
#   John 8:12 (NKJV) – “Then Jesus spoke to them again, saying, ‘I am the
#   light of the world. He who follows Me shall not walk in darkness, but
#   have the light of life.’”
#
#   Lesson 7 — A string such as "37" cannot turn itself into the integer
#   37. In a deeper way, we cannot raise ourselves from spiritual death
#   to life. We depend on the transforming work of Christ.
#   Ephesians 2:1, 5 (NKJV) – “And you He made alive, who were dead in
#   trespasses and sins… even when we were dead in trespasses, made us
#   alive together with Christ (by grace you have been saved).”
#
# Instructions for the Student:
#   1. Read each section before you run it.
#   2. Predict first. Write your guess in the comment.
#   3. Run the file and compare your guess with the printed output.
#   4. Complete every TODO. Replace the placeholder with real code.
#   5. Do not uncomment the ERROR examples. Those lines would stop the
#      file. They are there to read, not to run.
#   6. When you finish, check the SOLUTIONS section at the bottom.
#      Do not peek early. The struggle is the practice.
#
# Labs, Practice Files and Assessments are developed in collaboration
# with the Grok AI assistant under instructor supervision and review.
# =============================================================================

print("=" * 70)
print("PART 1: Four Basic Types")
print("=" * 70)

# int    — a whole number. No decimal point.
# float  — a number with a decimal point.
# str    — text inside quotes. Single or double quotes both work.
# bool   — only True or False. Both words start with a capital letter.

count = 7                 # int
price = 3.50              # float
label = "camper"          # str
active = True             # bool

print(count)
print(price)
print(label)
print(active)
# Predict the four lines: ________
# Actual:  7
#          3.5
#          camper
#          True
# Why:     print shows the value. 3.50 is stored as 3.5. Quotes do not print.

# A number in quotes is a string, not a number.
text_seven = "7"
real_seven = 7
print(text_seven)
print(real_seven)
# Predict: ________
# Actual:  7
#          7
# Why:     They look the same when printed. They are not the same type.
#          Part 2 will prove it.

# TODO 1: Create four variables and print each one.
#   apples        — an int
#   tax_rate      — a float
#   store_name    — a str
#   is_open       — a bool
# Write your eight lines below.


print("\n" + "=" * 70)
print("PART 2: Ask Python with type()")
print("=" * 70)

# type() reports the type. Read the output as "this value belongs to class ___."
print(type(7))
print(type(3.5))
print(type("7"))
print(type(True))
# Predict the four class names: ________
# Actual:  <class 'int'>
#          <class 'float'>
#          <class 'str'>
#          <class 'bool'>
# Why:     7 is an int. "7" is a str because of the quotes.

print(type(count))
print(type(price))
print(type(label))
print(type(active))
# Predict: ________
# Actual:  <class 'int'>
#          <class 'float'>
#          <class 'str'>
#          <class 'bool'>
# Why:     type() works on a variable the same way it works on a literal.

print(type(7) == int)
print(type("7") == int)
# Predict: ________
# Actual:  True
#          False
# Why:     7 is an int. "7" is not.

# TODO 2: Print the type of each value. Do not convert anything yet.
print("hello")      # TODO 2a: also print type(...)
print(0)            # TODO 2b: also print type(...)
print(0.0)          # TODO 2c: also print type(...)
print(False)        # TODO 2d: also print type(...)


print("\n" + "=" * 70)
print("PART 3: Types Decide What + Means")
print("=" * 70)

# The same symbol does different work for different types.
print(2 + 3)
# Predict: ________
# Actual:  5
# Why:     int + int is addition.

print("2" + "3")
# Predict: ________
# Actual:  23
# Why:     str + str is concatenation. The characters are joined. No space.

print(2.5 + 1.5)
# Predict: ________
# Actual:  4.0
# Why:     float + float stays a float.

# Mixing an int and a float is allowed. The result is a float.
print(2 + 3.0)
# Predict: ________
# Actual:  5.0
# Why:     Python promotes the int so both sides match.

# Mixing a number and a string is not allowed.
# Leave this line commented. Uncommenting it raises TypeError.
# print(2 + "3")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# TODO 3: Predict each result. Then run the file and fill Actual.
print(10 + 5)
# TODO 3a Predict: ________
# TODO 3a Actual:  ________

print("10" + "5")
# TODO 3b Predict: ________
# TODO 3b Actual:  ________

print(10.0 + 5)
# TODO 3c Predict: ________
# TODO 3c Actual:  ________


print("\n" + "=" * 70)
print("PART 4: bool Is Only True or False")
print("=" * 70)

# True and False are keywords. They must be capitalized exactly this way.
is_ready = True
has_error = False
print(is_ready)
print(has_error)
print(type(is_ready))
# Predict: ________
# Actual:  True
#          False
#          <class 'bool'>

# These lines are WRONG if you uncomment them.
# true = True          # this name is legal, but it is not the bool True
# print(true)          # it only works after you assign it
# print(True)          # this is the real bool
# print(true)          # NameError if the name was never assigned
# is_ready = true      # NameError — Python does not know "true"
# is_ready = "True"    # that is a string, not a bool

# TODO 4: Assign a bool named quiz_passed. Use True or False.
# Print the variable and print its type.


print("\n" + "=" * 70)
print("PART 5: int() — Make a Whole Number")
print("=" * 70)

# int() returns a new integer. It does not change the original value.
print(int("25"))
print(int(3.9))
print(int(3.1))
print(int(-3.9))
# Predict: ________
# Actual:  25
#          3
#          3
#          -3
# Why:     int("25") reads the digits.
#          int() on a float chops toward zero. It does not round.
#          3.9 becomes 3. -3.9 becomes -3.

raw_age = "16"
age = int(raw_age)
print(age)
print(type(age))
print(age + 1)
# Predict: ________
# Actual:  16
#          <class 'int'>
#          17
# Why:     After the conversion, + 1 is addition, not concatenation.

# These lines raise ValueError. Leave them commented.
# print(int("42.5"))     # ValueError: invalid literal for int() with base 10
# print(int("hello"))    # ValueError: the text is not a whole-number string
# print(int(""))         # ValueError: empty string
# print(int("  "))       # ValueError: whitespace only

# TODO 5: Convert the string "40" to an int, add 2, and print the sum.
# Expected output: 42
# Write your lines below.


print("\n" + "=" * 70)
print("PART 6: float() — Make a Decimal Number")
print("=" * 70)

print(float("2.5"))
print(float("9"))
print(float(7))
# Predict: ________
# Actual:  2.5
#          9.0
#          7.0
# Why:     float() can read "2.5" and "9". An int becomes a float with .0.

price_text = "9.99"
price_value = float(price_text)
print(price_value)
print(price_value * 2)
# Predict: ________
# Actual:  9.99
#          19.98
# Why:     Once it is a float, multiplication works.

# These lines raise ValueError. Leave them commented.
# print(float("nine"))
# print(float(""))

# TODO 6: Convert "3.25" to a float. Add 1.75. Print the result.
# Expected output: 5.0
# Write your lines below.


print("\n" + "=" * 70)
print("PART 7: str() — Make Text")
print("=" * 70)

# str() is the tool you need when you want to join a number onto a string
# with the + operator.
print(str(100))
print(str(3.14))
print(str(True))
print(type(str(100)))
# Predict: ________
# Actual:  100
#          3.14
#          True
#          <class 'str'>
# Why:     The printed characters look the same. The type is now str.

# Commas in print() already mix types. + does not.
print("Score:", 95)
print("Score: " + str(95))
# Predict: ________
# Actual:  Score: 95
#          Score: 95
# Why:     Both work. The + version needs str() because + concatenates.

# This line would raise TypeError. Leave it commented.
# print("Score: " + 95)

# TODO 7: Build one string that says  Year: 2026
# Use + and str(). Then print it.
# Expected output: Year: 2026
# Write your line below.


print("\n" + "=" * 70)
print("PART 8: bool() — Ask If a Value Counts as True")
print("=" * 70)

# bool() is useful later with if statements. Learn the pattern now.
print(bool(1))
print(bool(0))
print(bool(3.14))
print(bool(0.0))
print(bool("hello"))
print(bool(""))
print(bool("0"))
print(bool(True))
print(bool(False))
# Predict each True or False: ________
# Actual:  True
#          False
#          True
#          False
#          True
#          False
#          True
#          True
#          False
# Why:     0, 0.0, "", and False become False.
#          Almost every other value becomes True.
#          The string "0" is not empty, so it is True.
#          The string "False" would also be True — it is not empty.

# TODO 8: Print bool() of each of these values: 12, 0, "yes", ""
# Write four print lines below.


print("\n" + "=" * 70)
print("PART 9: Convert in Steps When One Call Is Not Enough")
print("=" * 70)

# int() cannot read "42.5" because of the decimal point.
# float() can. Then int() can chop the float.
print(float("42.5"))
print(int(float("42.5")))
print(int(float("42.9")))
# Predict: ________
# Actual:  42.5
#          42
#          42
# Why:     Two conversions. First become a float. Then become an int.
#          The second step still chops toward zero. It does not round.

# TODO 9: The string "18.7" should become the integer 18.
# Use two conversions. Print the integer.
# Expected output: 18
# Write your line below.


print("\n" + "=" * 70)
print("PART 10: A Small Real Task")
print("=" * 70)

# Pretend these strings came from input(). input() always returns a str.
# Convert them before you calculate.

qty_text = "4"
item_price_text = "2.50"
tax_text = "0.08"

# TODO 10a: Convert qty_text to an int named qty.
# TODO 10b: Convert item_price_text to a float named item_price.
# TODO 10c: Convert tax_text to a float named tax_rate.
# TODO 10d: Compute subtotal = qty * item_price and print it.
#           Expected: 10.0
# TODO 10e: Compute total = subtotal + (subtotal * tax_rate) and print it.
#           Expected: 10.8
# Write your lines below.


print("\n" + "=" * 70)
print("PART 11: Your Turn — Mixed Practice")
print("=" * 70)

# TODO 11: Print the type of "3.14". Then convert it to a float and
# print the type again.
# Expected types: <class 'str'> then <class 'float'>


# TODO 12: What does int(9.8) print? Write a print and a prediction.
# TODO 12 prediction: ________
# Expected: 9


# TODO 13: Join the word Chapter and the number 2 with +.
# Expected output: Chapter 2
# Hint: you need a space and you need str().


# TODO 14: True or False — after this line, kind is a bool.
#   kind = bool("False")
# Write True or False in the comment, then print kind and type(kind).
# TODO 14 answer: ________


print("\n" + "=" * 70)
print("Great work.")
print("Check the type before you choose the operation.")
print("Convert on purpose. Do not hope Python will guess.")
print("John 8:12 — light shows what a thing really is.")
print("Ephesians 2:1, 5 — the change we need is given, not self-made.")
print("=" * 70)


# =============================================================================
# SOLUTIONS
# Check these only after you have written your own predictions and code.
# =============================================================================
#
# PART 1
#   Printed: 7 / 3.5 / camper / True
#   Printed: 7 / 7   (same look, different types)
#   TODO 1 example:
#       apples = 12
#       tax_rate = 0.05
#       store_name = "Call's Grocery"
#       is_open = True
#       print(apples)
#       print(tax_rate)
#       print(store_name)
#       print(is_open)
#
# PART 2
#   type(7)      →  <class 'int'>
#   type(3.5)    →  <class 'float'>
#   type("7")    →  <class 'str'>
#   type(True)   →  <class 'bool'>
#   type(...) == int  →  True then False
#   TODO 2a  print(type("hello"))   →  <class 'str'>
#   TODO 2b  print(type(0))         →  <class 'int'>
#   TODO 2c  print(type(0.0))       →  <class 'float'>
#   TODO 2d  print(type(False))     →  <class 'bool'>
#
# PART 3
#   2 + 3          →  5
#   "2" + "3"      →  23
#   2.5 + 1.5      →  4.0
#   2 + 3.0        →  5.0
#   TODO 3a  15
#   TODO 3b  105
#   TODO 3c  15.0
#
# PART 4
#   Printed: True / False / <class 'bool'>
#   TODO 4 example:
#       quiz_passed = True
#       print(quiz_passed)
#       print(type(quiz_passed))
#
# PART 5
#   int("25")   →  25
#   int(3.9)    →  3
#   int(3.1)    →  3
#   int(-3.9)   →  -3
#   age + 1     →  17
#   TODO 5 example:
#       print(int("40") + 2)
#
# PART 6
#   float("2.5")  →  2.5
#   float("9")    →  9.0
#   float(7)      →  7.0
#   price * 2     →  19.98
#   TODO 6 example:
#       print(float("3.25") + 1.75)
#
# PART 7
#   str(100)          →  "100"   type is str
#   "Score:" versions both print Score: 95
#   TODO 7 example:
#       print("Year: " + str(2026))
#
# PART 8
#   bool(1)       →  True
#   bool(0)       →  False
#   bool(3.14)    →  True
#   bool(0.0)     →  False
#   bool("hello") →  True
#   bool("")      →  False
#   bool("0")     →  True
#   bool(True)    →  True
#   bool(False)   →  False
#   TODO 8:
#       print(bool(12))      # True
#       print(bool(0))       # False
#       print(bool("yes"))   # True
#       print(bool(""))      # False
#
# PART 9
#   float("42.5")         →  42.5
#   int(float("42.5"))    →  42
#   int(float("42.9"))    →  42
#   TODO 9 example:
#       print(int(float("18.7")))
#
# PART 10
#   qty = int(qty_text)
#   item_price = float(item_price_text)
#   tax_rate = float(tax_text)
#   subtotal = qty * item_price
#   print(subtotal)                          # 10.0
#   total = subtotal + (subtotal * tax_rate)
#   print(total)                             # 10.8
#
# PART 11
#   TODO 11:
#       print(type("3.14"))
#       print(type(float("3.14")))
#   TODO 12:
#       print(int(9.8))                      # 9
#   TODO 13:
#       print("Chapter " + str(2))
#   TODO 14:
#       False — kind is a bool, yes, but bool("False") is True
#       because the string is not empty.
#       print(kind)        # True
#       print(type(kind))  # <class 'bool'>
#
# =============================================================================

# Copyright 2026 LogosTeach - All Rights Reserved
