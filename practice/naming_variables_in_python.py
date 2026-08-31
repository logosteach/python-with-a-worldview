# =============================================================================
# Practice: Naming Variables in Python
# Unit 2  ·  Lesson 2  ·  Foundational Elements
# =============================================================================
# Learning Objectives:
#   - Declare a variable and assign a value with a single equals sign.
#   - Tell a legal name from an illegal name before you run the line.
#   - Apply snake_case and other course conventions (PEP 8).
#   - Avoid Python keywords and built-in names such as print and input.
#   - Distinguish SyntaxError from NameError.
#   - Reassign a name and trace the new value.
#
# Biblical Connection:
#   2 Corinthians 1:20 (NKJV) – “For all the promises of God in Him are
#   Yes, and in Him Amen, to the glory of God through us.”
#   A variable name can point to a new value on the next line. The promises
#   of God in Christ are not reassigned. They stay Yes and Amen.
#
# Instructions for the Student:
#   1. Read each section before you run it.
#   2. Predict first. Write your guess in the comment.
#   3. Complete every TODO. Replace the placeholder with real code.
#   4. Do not uncomment the ILLEGAL examples. Those lines are there to
#      read, not to run. They would stop the file with a SyntaxError.
#   5. When you finish, check the SOLUTIONS section at the bottom.
#      Do not peek early. The struggle is the practice.
#
# Labs, Practice Files and Assessments are developed in collaboration
# with the Grok AI assistant under instructor supervision and review.
# =============================================================================

print("=" * 70)
print("PART 1: A Variable Is a Name That Refers to a Value")
print("=" * 70)

# Assignment uses one equals sign. Read it as "gets," not "equals."
first_name = "Hannah"
age = 15
quiz_score = 92.5

print(first_name)
print(age)
print(quiz_score)
# Predict the three lines of output: ________
# Actual:  Hannah
#          15
#          92.5
# Why:     print uses the name. The value comes out, not the word first_name.

# TODO 1: Create a variable called favorite_color and assign a string.
# Then print it.
# Write your two lines below.


print("\n" + "=" * 70)
print("PART 2: Syntax Rules — Legal vs Illegal")
print("=" * 70)

# Legal names use letters, digits, and underscores.
# They must start with a letter or an underscore.
score2 = 10
my_score = 88
_total = 100
print(score2, my_score, _total)
# Predict: ________
# Actual:  10 88 100

# These lines are ILLEGAL. Leave them commented.
# If you remove the #, Python stops with SyntaxError.
# 2score = 10          # cannot start with a digit
# first-name = "Eli"   # hyphen is not allowed
# user name = "Ada"    # spaces are not allowed
# my@var = 5           # @ is not allowed
# for = 10             # for is a reserved word (keyword)

# TODO 2: For each name, write LEGAL or ILLEGAL in the comment.
# name_a = "score2"        # TODO 2a: ________
# name_b = "2score"        # TODO 2b: ________
# name_c = "my-score"      # TODO 2c: ________
# name_d = "my_score"      # TODO 2d: ________
# name_e = "first name"    # TODO 2e: ________
# name_f = "for"           # TODO 2f: ________


print("\n" + "=" * 70)
print("PART 3: Case-Sensitive Names")
print("=" * 70)

Score = 90
score = 80
print(Score, score)
# Predict: ________
# Actual:  90 80
# Why:     Score and score are two different names.

# This would raise NameError if you ran it. Leave it commented.
# print(SCORE)
# Why: SCORE was never assigned. Wrong capitalization is a new name.

# TODO 3: Assign midterm_score the value 87. Print midterm_score.
# Do not print Midterm_Score. That would be a different name.
# Write your two lines below.


print("\n" + "=" * 70)
print("PART 4: Convention — snake_case and Good Names")
print("=" * 70)

# Python will accept totalSum. This course still wants total_sum.
total_sum = 25 + 17
first_name_again = "Eli"
MAX_SCORE = 100
print(total_sum)
print(first_name_again)
print(MAX_SCORE)

# Poor style (do not copy these habits):
# totalSum = 42        # camelCase — legal, not course style
# print = 10           # shadows the built-in print()
# l = 5                # looks like the digit 1
# fn = "Ada"           # too short to describe the value

# TODO 4: Rewrite each poor name in snake_case. Assign a simple value.
#   quizScore      ->  ________
#   HomeAddress    ->  ________
#   USERNAME wait: that one is a constant style. Use UPPER_SNAKE_CASE.
# Write three assignment lines below.


print("\n" + "=" * 70)
print("PART 5: Keywords and Built-ins")
print("=" * 70)

# Keywords already belong to Python. You cannot use them as names.
# See the list anytime with:  help("keywords")
# Examples: if, else, for, while, class, def, import, True, False, None

# Built-in names are different. This line is legal and is a bad idea:
# print = 10
# Later, print("hello") would break because print no longer means the function.

# TODO 5: Circle (in the comment) which names you must not use.
#   age          # TODO 5a: OK or DO NOT USE? ________
#   for          # TODO 5b: ________
#   input        # TODO 5c: ________
#   class        # TODO 5d: ________
#   student_id   # TODO 5e: ________


print("\n" + "=" * 70)
print("PART 6: Reassignment — The Name Stays, the Value Can Change")
print("=" * 70)

points = 10
print("Start:", points)
# Predict: ________
# Actual:  Start: 10

points = points + 5
print("After bonus:", points)
# Predict: ________
# Actual:  After bonus: 15
# Why:     Python reads the old 10, adds 5, and stores 15 back in points.

points = 100
print("Reset:", points)
# Predict: ________
# Actual:  Reset: 100

# TODO 6: Start lives at 3. Add 2 using lives = lives + 2. Then print lives.
# Expected printed value: 5
# Write your three lines below.


print("\n" + "=" * 70)
print("PART 7: Use Names in an Expression")
print("=" * 70)

width = 8
height = 5
area = width * height
print("Area:", area)
print(width, "x", height, "=", area)
# Predict the two printed lines: ________
# Actual:  Area: 40
#          8 x 5 = 40

# TODO 7: Store length = 12 and width_box = 4.
# Compute perimeter = 2 * (length + width_box) and print it.
# Expected: 32
# Write your lines below.


print("\n" + "=" * 70)
print("PART 8: Your Turn — Repair the Names")
print("=" * 70)

# Each TODO shows a broken idea. Write a LEGAL, course-style version.

# TODO 8: A student's first name should be stored.
# Broken idea:  1st-name = "Ruth"
# Write a legal assignment and print the name.


# TODO 9: A quiz score of 95.
# Broken idea:  Quiz Score = 95
# Write a legal assignment and print the score.


# TODO 10: Count of completed labs.
# Broken idea:  for = 4
# Write a legal assignment and print the count.


print("\n" + "=" * 70)
print("Great work.")
print("Legal first. Then snake_case. Then trace the name after every =.")
print("2 Corinthians 1:20 — variables can change. His promises do not.")
print("=" * 70)


# =============================================================================
# SOLUTIONS
# Check these only after you have written your own names and predictions.
# =============================================================================
#
# PART 1
#   Printed: Hannah / 15 / 92.5
#   TODO 1 example:
#       favorite_color = "blue"
#       print(favorite_color)
#
# PART 2
#   Printed: 10 88 100
#   TODO 2a LEGAL
#   TODO 2b ILLEGAL  (starts with a digit)
#   TODO 2c ILLEGAL  (hyphen)
#   TODO 2d LEGAL
#   TODO 2e ILLEGAL  (space)
#   TODO 2f ILLEGAL  (keyword)
#
# PART 3
#   Printed: 90 80
#   TODO 3 example:
#       midterm_score = 87
#       print(midterm_score)
#
# PART 4
#   TODO 4 example:
#       quiz_score = 88
#       home_address = "12 Oak St"
#       USER_NAME = "eli"
#
# PART 5
#   TODO 5a OK
#   TODO 5b DO NOT USE  (keyword)
#   TODO 5c DO NOT USE  (built-in — convention)
#   TODO 5d DO NOT USE  (keyword)
#   TODO 5e OK
#
# PART 6
#   Start: 10
#   After bonus: 15
#   Reset: 100
#   TODO 6 example:
#       lives = 3
#       lives = lives + 2
#       print(lives)          # 5
#
# PART 7
#   Area: 40
#   8 x 5 = 40
#   TODO 7 example:
#       length = 12
#       width_box = 4
#       perimeter = 2 * (length + width_box)
#       print(perimeter)      # 32
#
# PART 8
#   TODO 8 example:
#       first_name = "Ruth"
#       print(first_name)
#   TODO 9 example:
#       quiz_score = 95
#       print(quiz_score)
#   TODO 10 example:
#       labs_completed = 4
#       print(labs_completed)
#
# =============================================================================

# Copyright 2026 LogosTeach - All Rights Reserved
