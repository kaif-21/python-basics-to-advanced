# Day 1: Python Basics
# Topic: Basic Syntax, Variables, Data Types, Operators

# -----------------------------
# Case Sensitivity
# Python is case-sensitive
age = 23
Age = 25
print(age)
print(Age)

# -----------------------------
# Indentation
# Python uses indentation to define blocks of code
# Usually 4 spaces are used

if True:
    print("Correct indentation")
else:
    print("Incorrect indentation")

# -----------------------------
# Line Continuation
# Use backslash (\) to continue a statement to the next line

total = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + \
        56 + 54 + 34 + 32
print("Total:", total)

# -----------------------------
# Multiple statements on a single line

x = 4; y = 5; z = 6
print(x, y, z)

# -----------------------------
# Variable Assignment

age = 23          # integer
name = "Kaif"     # string
is_student = True # boolean

print(age)
print(name)
print(is_student)

# -----------------------------
# Type Inference
# Python automatically detects the data type

print(type(age))
print(type(name))
print(type(is_student))

# -----------------------------
# NameError Example
# Uncommenting the below line will cause NameError
# because 'b' is not defined

# a = b

# -----------------------------
# End of Day 1
