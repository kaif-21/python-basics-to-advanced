# =========================================
# Lesson 2: Control Statements & Loops
# =========================================

# Assignment 1: if Statement
# Check whether a number is positive
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")

# Assignment 2: if-else Statement
# Check whether a number is positive or negative
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
else:
    print("Negative")

# Assignment 3: if-elif-else Statement
# Check whether a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# Assignment 4: Nested if Statement
# Check whether number is positive & even/odd or negative
num = int(input("Enter a number: "))
if num >= 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Negative")

# Assignment 5: for Loop
# Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Assignment 6: while Loop
# Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# Assignment 7: Nested Loops
# Print 5x5 grid of *
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

# Assignment 8: break Statement
# Sum numbers until user enters 0
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Sum:", total)

# Assignment 9: continue Statement
# Print numbers 1 to 10 except 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Assignment 10: pass Statement
# Empty function
def empty_function():
    pass

# Assignment 11: Loops + Conditionals
# Print even numbers up to n
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

# Assignment 12: Factorial Calculation
# Calculate factorial using loop
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)

# Assignment 13: Sum of Digits
# Calculate sum of digits
num = int(input("Enter a number: "))
digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num //= 10
print("Sum of digits:", digit_sum)

# Assignment 14: Prime Number Check
# Check whether number is prime
num = int(input("Enter a number: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")

# Assignment 15: Fibonacci Sequence
# Print first n Fibonacci numbers
n = int(input("Enter how many Fibonacci numbers: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
