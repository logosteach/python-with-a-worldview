# =============================================================================
# Practice: Order of Operations in Python
# Unit 2  ·  Lesson 1  ·  Foundational Elements
# =============================================================================
# Learning Objectives:
#   - Explain how Python ranks +, -, *, /, //, %, and ** (PEMDAS).
#   - Use parentheses to force the order you actually mean.
#   - Evaluate a multi-operator expression by hand, then confirm with print().
#   - Identify common precedence mistakes, especially missing parentheses
#     around a sum before division.
#   - Remember that ** is right-associative, while * / // % and + - walk
#     left to right.
#
# Biblical Connection:
#   John 16:12 (NKJV) – “I still have many things to say to you, but you
#   cannot bear them now.”
#   Some operations must finish before others begin. Skipping a required
#   step makes the result wrong. Waiting on the Lord’s timing is part of
#   walking with Him.
#
# Instructions for the Student:
#   1. Read each section before you run it.
#   2. Predict the result on paper FIRST. Write your guess in the comment.
#   3. Run the file and compare your guess with the printed output.
#   4. Complete every TODO. Replace the placeholder with real code.
#   5. When you finish, check the SOLUTIONS section at the bottom.
#      Do not peek early. The struggle is the practice.
# =============================================================================

print("=" * 70)
print("PART 1: Python Does Not Always Read Left to Right")
print("=" * 70)

# Multiplication outranks addition. The * finishes before the +.
print(2 + 3 * 4)
# Predict: ________
# Actual:  14
# Why:     3 * 4 is 12, then 2 + 12 is 14. Not 20.

# Parentheses lift the addition above the multiply.
print((2 + 3) * 4)
# Predict: ________
# Actual:  20
# Why:     (2 + 3) is 5, then 5 * 4 is 20.

# True division also outranks addition and subtraction.
print(10 - 8 / 2)
# Predict: ________
# Actual:  6.0
# Why:     8 / 2 is 4.0, then 10 - 4.0 is 6.0. Notice the result is a float.


print("\n" + "=" * 70)
print("PART 2: Same Rank Walks Left to Right")
print("=" * 70)

# + and - share a rank. Python walks from the left.
print(10 - 4 + 2)
# Predict: ________
# Actual:  8
# Why:     (10 - 4) + 2. Not 10 - 6.

# * and / share a rank. Same left-to-right rule.
print(10 / 2 * 5)
# Predict: ________
# Actual:  25.0
# Why:     (10 / 2) * 5. Not 10 / 10.

# // sits with * and /. It does not wait for + or -.
print(20 // 4 // 2)
# Predict: ________
# Actual:  2
# Why:     (20 // 4) // 2  →  5 // 2  →  2.

# % also sits with * and /.
print(17 % 5 * 2)
# Predict: ________
# Actual:  4
# Why:     (17 % 5) * 2  →  2 * 2  →  4.


print("\n" + "=" * 70)
print("PART 3: Floor Division and Remainder in the Lineup")
print("=" * 70)

# // asks: how many whole groups fit? The leftover is thrown away.
print(17 // 5)
# Predict: ________
# Actual:  3

# % asks: what is left after the whole groups are taken?
print(17 % 5)
# Predict: ________
# Actual:  2

# Check: 3 groups of 5, plus a remainder of 2, rebuilds 17.
print(3 * 5 + 2)
# Predict: ________
# Actual:  17

# Because // and % outrank +, they finish first in these lines.
print(10 + 17 // 5)
# Predict: ________
# Actual:  13
# Why:     17 // 5 is 3, then 10 + 3.

print(10 + 17 % 5)
# Predict: ________
# Actual:  12
# Why:     17 % 5 is 2, then 10 + 2.

# Parentheses pull the addition up first.
print((10 + 17) // 5)
# Predict: ________
# Actual:  5


print("\n" + "=" * 70)
print("PART 4: Powers Run High — and Right to Left")
print("=" * 70)

# ** outranks * / // % and + -.
print(2 ** 3)
# Predict: ________
# Actual:  8

# Stacked ** is the one operator in this lesson that looks RIGHT first.
print(2 ** 3 ** 2)
# Predict: ________
# Actual:  512
# Why:     2 ** (3 ** 2)  →  2 ** 9  →  512.

# Parentheses change the power.
print((2 ** 3) ** 2)
# Predict: ________
# Actual:  64
# Why:     (2 ** 3) is 8, then 8 ** 2 is 64.

# Mix ** with * and the power still finishes first.
print(2 ** 3 * 2)
# Predict: ________
# Actual:  16
# Why:     (2 ** 3) * 2  →  8 * 2  →  16. Not 2 ** 6.


print("\n" + "=" * 70)
print("PART 5: Parentheses Make Intent Visible")
print("=" * 70)

# An average is a sum divided by a count.
# Without parentheses, only the last score is divided.
score1 = 80
score2 = 90
score3 = 100

wrong = score1 + score2 + score3 / 3
right = (score1 + score2 + score3) / 3

print("Without parentheses:", wrong)
print("With parentheses:   ", right)
# Predict wrong: ________
# Predict right: ________
# Actual wrong:  203.333...
# Actual right:  90.0
# Why:  100 / 3 happens first unless the sum is wrapped.


print("\n" + "=" * 70)
print("PART 6: Trace One Expression by Hand")
print("=" * 70)

# Work this on paper before you look at the comments under it.
result = 5 + 2 * 3 ** 2 - 8 / 4
print(result)
# Step 1.  ** first:          3 ** 2          →  9
# Step 2.  * and / next:      2 * 9  and  8 / 4  →  18  and  2.0
# Step 3.  + and - last:      5 + 18 - 2.0    →  21.0
# Actual:  21.0

# Change the grouping and the story changes.
result2 = (5 + 2) * (3 ** 2 - 8) / 4
print(result2)
# Step 1.  insides first:     (5 + 2) is 7,  (9 - 8) is 1
# Step 2.  7 * 1 / 4          →  1.75
# Actual:  1.75


print("\n" + "=" * 70)
print("PART 7: Your Turn — Predict, Then Confirm")
print("=" * 70)

# TODO 1: Write your prediction in the comment. Then run.
print(1 + 2 * 3)
# TODO 1 prediction: ________
# Expected after you check the solutions: 7

# TODO 2
print(10 / (2 * 5))
# TODO 2 prediction: ________
# Expected: 1.0

# TODO 3
print(4 ** 2 + 3 * 2)
# TODO 3 prediction: ________
# Expected: 22

# TODO 4
print(18 // 4 + 18 % 4)
# TODO 4 prediction: ________
# Expected: 6

# TODO 5
print(3 ** 2 ** 2)
# TODO 5 prediction: ________
# Expected: 81


print("\n" + "=" * 70)
print("PART 8: Your Turn — Write the Expression")
print("=" * 70)

# TODO 6: Print the average of 70, 85, and 90. Use parentheses.
# Expected output: 81.666...
# Write your line below.


# TODO 7: Print 2 to the power of 5, then multiply that result by 3.
# Do not use extra parentheses unless you want them.
# Expected output: 96
# Write your line below.


# TODO 8: How many whole weeks are in 20 days? Use // .
# Expected output: 2
# Write your line below.


# TODO 9: How many leftover days after those whole weeks? Use % .
# Expected output: 6
# Write your line below.


# TODO 10: Write one print() that adds 4 and 6 first, then raises
# that sum to the power of 2. Expected output: 100
# Write your line below.


print("\n" + "=" * 70)
print("Great work.")
print("Predict on paper. Then let print() confirm the ranking.")
print("If paper and Python disagree, check the order — not the computer.")
print("John 16:12 — some steps must wait until the right time.")
print("=" * 70)


# =============================================================================
# SOLUTIONS
# Check these only after you have written your own predictions and code.
# =============================================================================
#
# PART 1
#   2 + 3 * 4          →  14
#   (2 + 3) * 4        →  20
#   10 - 8 / 2         →  6.0
#
# PART 2
#   10 - 4 + 2         →  8
#   10 / 2 * 5         →  25.0
#   20 // 4 // 2       →  2
#   17 % 5 * 2         →  4
#
# PART 3
#   17 // 5            →  3
#   17 % 5             →  2
#   3 * 5 + 2          →  17
#   10 + 17 // 5       →  13
#   10 + 17 % 5        →  12
#   (10 + 17) // 5     →  5
#
# PART 4
#   2 ** 3             →  8
#   2 ** 3 ** 2        →  512
#   (2 ** 3) ** 2      →  64
#   2 ** 3 * 2         →  16
#
# PART 5
#   wrong              →  203.333...
#   right              →  90.0
#
# PART 6
#   result             →  21.0
#   result2            →  1.75
#
# PART 7
#   TODO 1   1 + 2 * 3           →  7
#   TODO 2   10 / (2 * 5)        →  1.0
#   TODO 3   4 ** 2 + 3 * 2      →  22     (16 + 6)
#   TODO 4   18 // 4 + 18 % 4    →  6      (4 + 2)
#   TODO 5   3 ** 2 ** 2         →  81     (3 ** 4, because ** is right-associative)
#
# PART 8
#   TODO 6   print((70 + 85 + 90) / 3)
#   TODO 7   print(2 ** 5 * 3)
#   TODO 8   print(20 // 7)
#   TODO 9   print(20 % 7)
#   TODO 10  print((4 + 6) ** 2)
#
# =============================================================================

# Copyright 2026 LogosTeach - All Rights Reserved

# Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.
