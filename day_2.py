# Day 2: Variables, Operators, Conditions and Loops

# ---------------------------------
# Declaring and Assigning Variables
age = 32
height = 5.8
name = "Kaif"
is_student = True

print("Age:", age)
print("Height:", height)
print("Name:", name)
print("Is Student:", is_student)

# ---------------------------------
# Naming Conventions
# Valid variable names
first_name = "Kaif"
last_name = "Chouhan"

# Invalid variable names (examples)
# 2age = 30
# first-name = "Kaif"
# @name = "Kaif"

# ---------------------------------
# Case Sensitivity
name = "kaif"
Name = "chouhan"
print(name)
print(Name)

# ---------------------------------
# Dynamic Typing
age = 23          # int
height = 5.8      # float
name = "Kaif"     # string
is_student = True # boolean

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

# ---------------------------------
# User Input
user_age = int(input("Enter your age: "))
print("Your age is:", user_age)

# ---------------------------------
# Arithmetic Operators
a = 5
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Exponent:", a ** b)
print("Modulus:", a % b)

# ---------------------------------
# Logical Operators
x = False
y = True

print("x or y:", x or y)
print("x and y:", x and y)
print("not x:", not x)

# ---------------------------------
# Conditional Statements
num = int(input("Enter a number: "))

if num >= 0:
    print("Number is positive")
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is negative")

# ---------------------------------
# Simple Calculator
op = input("Select operation (+, -, *, /, //, %, **): ")

if op not in ("+", "-", "*", "/", "//", "%", "**"):
    print("Invalid operator")
else:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "//":
        print(num1 // num2)
    elif op == "%":
        print(num1 % num2)
    elif op == "**":
        print(num1 ** num2)

# ---------------------------------
# For Loop
for i in range(5):
    print(i)

# ---------------------------------
# While Loop
count = 0
while count <= 5:
    print(count)
    count += 1

# ---------------------------------
# Loop Control Statements
# Break
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# ---------------------------------
# Nested Loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# ---------------------------------
# Sum of First 10 Natural Numbers
n = 10
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of first 10 natural numbers:", total)

# ---------------------------------
# Prime Numbers Between 1 and 100
for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
