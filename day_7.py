
# ===============================
# FUNCTIONS IN PYTHON
# ===============================


# definition
# a function is a block code that performs a specific task. function help in organization code,reusing code and improving readability



# 1. Variable length arguments (*args)
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5, "kaif")


# 2. Positional + Keyword arguments
def print_details(*args, **kwargs):
    for val in args:
        print(f"Positional argument: {val}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(1, 2, "kaif", name="Kaif", age=21, country="India")


# 3. Return multiple values
def multiply(a, b):
    return a * b, a

print(multiply(10, 5))


# 4. Temperature conversion
def convert_temperature(temp, unit):
    if unit == "C":
        return (temp * 9 / 5) + 32
    elif unit == "F":
        return (temp - 32) * 5 / 9
    else:
        return None

print(convert_temperature(27, "C"))
print(convert_temperature(77, "F"))


# 5. Password strength checker
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in "@#$!%&*()_" for char in password):
        return False
    return True

print(is_strong_password("weakpwd"))
print(is_strong_password("Str0ngPwd!"))


# 6. Shopping cart total cost
def calculate_total_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost += item['price'] * item['quantity']
    return total_cost

cart = [
    {'name': 'apple', 'price': 0.5, 'quantity': 2},
    {'name': 'banana', 'price': 0.3, 'quantity': 12},
    {'name': 'orange', 'price': 0.6, 'quantity': 20}
]

print(calculate_total_cost(cart))


# 7. Palindrome check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("a man a plan a canal panama"))
print(is_palindrome("hello world"))


# 8. Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


