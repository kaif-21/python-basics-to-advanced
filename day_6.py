# Day 6 – Python Dictionaries

"""
Dictionaries are unordered collections of items.
They store data in key-value pairs.
Keys must be unique and immutable (string, number, or tuple).
Values can be of any type.
"""

# -------------------------
# Creating Dictionaries
# -------------------------

# Example of a dictionary
student = {"name": "Kaif Chouhan", "age": 22, "grade": 23}
print("Student dictionary:", student)

# -------------------------
# Accessing Elements
# -------------------------

# Using square brackets
print("Grade:", student['grade'])

# Using get() method
print("Grade (get method):", student.get('grade'))
print("Last Name (get method, not present):", student.get('last_name'))
print("Last Name with default:", student.get('last_name', "Not Available"))

# -------------------------
# Modifying Dictionary
# -------------------------

# Update existing key
student["age"] = 23
print("Updated age:", student)

# Add new key-value pair
student["address"] = "India"
print("Added address:", student)

# Delete a key
del student["grade"]
print("After deleting grade:", student)

# -------------------------
# Dictionary Methods
# -------------------------

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# -------------------------
# Copying Dictionaries
# -------------------------

# Reference copy
student_copy = student
student["name"] = "Kaif"
print("Original:", student)
print("Reference copy:", student_copy)

# Shallow copy
student_copy = student.copy()
student["name"] = "Kaif3"
print("Original after modification:", student)
print("Shallow copy:", student_copy)

# -------------------------
# Iterating over Dictionaries
# -------------------------

# Iterate over keys
for key in student.keys():
    print("Key:", key)

# Iterate over values
for value in student.values():
    print("Value:", value)

# Iterate over key-value pairs
for key, value in student.items():
    print("Key:", key, "Value:", value)

# -------------------------
# Nested Dictionaries
# -------------------------

students = {
    "student1": {"name": "Kaif Chouhan", "age": 22, "grade": 23},
    "student2": {"name": "Danish", "age": 34, "grade": 24},
}

print("Nested Dictionary:", students)
print("Student1 Name:", students["student1"]["name"])
print("Student1 Age:", students["student1"]["age"])

# Iterating over nested dictionaries
for student_id, info in students.items():
    print(f"{student_id}: {info}")
    for key, value in info.items():
        print(f"  {key}: {value}")

# -------------------------
# Dictionary Comprehensions
# -------------------------

# Basic comprehension
squares = {x: x**2 for x in range(5)}
print("Squares:", squares)

# Conditional comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Even Squares:", even_squares)

# -------------------------
# Practical Examples
# -------------------------

# Count frequency of elements in a list
numbers = [1,1,2,2,3,3,4,4,5,5]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
print("Frequency:", frequency)

# Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)
