"""
Lambda Functions, map(), and filter() in Python
"""

# ----------------------------
# Normal function vs Lambda
# ----------------------------

def addition(a, b):
    return a + b

print(addition(3, 6))


addition_lambda = lambda a, b: a + b
print(addition_lambda(3, 6))


# ----------------------------
# Even number check
# ----------------------------

def is_even(num):
    return num % 2 == 0

print(is_even(24))


is_even_lambda = lambda num: num % 2 == 0
print(is_even_lambda(12))


# ----------------------------
# Multiple arguments
# ----------------------------

def add_three(x, y, z):
    return x + y + z

print(add_three(1, 2, 3))


add_three_lambda = lambda x, y, z: x + y + z
print(add_three_lambda(4, 5, 6))


# ----------------------------
# map() examples
# ----------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def square(num):
    return num ** 2

print(square(10))
print(list(map(square, numbers)))


# map() with lambda
print(list(map(lambda x: x ** 2, numbers)))


# map() with multiple iterables
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]

added_numbers = list(map(lambda x, y: x + y, numbers1, numbers2))
print(added_numbers)


# map() string to int
str_numbers = ["1", "4", "4", "7"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)


# map() on strings
words = ["apple", "banana", "orange"]
upper_words = list(map(str.upper, words))
print(upper_words)


# map() with dictionary data
def get_name(person):
    return person["name"]

people = [
    {"name": "kaif", "age": 21},
    {"name": "aman", "age": 22}
]

print(list(map(get_name, people)))


# ----------------------------
# filter() examples
# ----------------------------

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(is_even, lst)))


# filter() with lambda
greater_than_five = list(filter(lambda x: x > 5, lst))
print(greater_than_five)


even_and_greater_than_five = list(
    filter(lambda x: x > 5 and x % 2 == 0, lst)
)
print(even_and_greater_than_five)


# filter() with dictionary
people = [
    {"name": "kaif", "age": 21},
    {"name": "aman", "age": 22},
    {"name": "khan", "age": 56}
]

def age_greater_than_25(person):
    return person["age"] > 25

print(list(filter(age_greater_than_25, people)))
