# ==============================
# ITERATORS
# ==============================

print("----- ITERATORS -----")

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("Iterator is empty")


# String Iterator
my_string = "kaif"
it = iter(my_string)

print(next(it))
print(next(it))
print(next(it))
print(next(it))


# ==============================
# GENERATORS
# ==============================

print("\n----- GENERATORS -----")

def square(n):
    for i in range(n):
        yield i**2

gen = square(3)

print(next(gen))
print(next(gen))
print(next(gen))

print("Using loop:")
for i in square(3):
    print(i)


def my_generators():
    yield 1
    yield 2
    yield 3

gen2 = my_generators()

print(next(gen2))
print(next(gen2))
print(next(gen2))

# Generator exhaust ho chuka hai
for val in gen2:
    print(val)   # kuch print nahi hoga


# Practical Example: Reading Large File
print("\n----- READING LARGE FILE USING GENERATOR -----")

def read_large_file(file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:
                yield line
    except FileNotFoundError:
        print("file.txt not found. Create one to test this example.")

file_path = "file.txt"

for line in read_large_file(file_path):
    print(line.strip())


# ==============================
# FUNCTION COPY
# ==============================

print("\n----- FUNCTION COPY -----")

def welcome():
    return "Welcome to Advanced Python"

wel = welcome   # function copy
del welcome     # original delete

print(wel())


# ==============================
# CLOSURES
# ==============================

print("\n----- CLOSURES -----")

def main_welcome(func):

    def sub_welcome_method():
        print("Welcome")
        func("Hello everyone")
        print("Please learn these concepts properly")

    return sub_welcome_method

closure_func = main_welcome(print)
closure_func()


# ==============================
# DECORATORS
# ==============================

print("\n----- BASIC DECORATOR -----")

def main_decorator(func):

    def wrapper():
        print("Welcome")
        func()
        print("Please learn these concepts properly")

    return wrapper


@main_decorator
def course_introduction():
    print("Introduction to Advanced Python")

course_introduction()


# Another Decorator Example
print("\n----- CUSTOM DECORATOR -----")

def my_decorator(func):

    def wrapper():
        print("Hello")
        func()
        print("Song sunega??")

    return wrapper


@my_decorator
def say_hello():
    print("Hello")

say_hello()


# ==============================
# DECORATOR WITH ARGUMENTS
# ==============================

print("\n----- DECORATOR WITH ARGUMENTS -----")

def repeat(n):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello")

greet()
