# =====================================================
# Module 3: Data Structures Assignmentss
# Lesson 3.3: Sets
# =====================================================

# -----------------------------------------------------
# Assignment 1: Creating and Accessing Sets
# Create a set with the first 10 positive integers.
# -----------------------------------------------------
s = set(range(1, 11))
print(s)


# -----------------------------------------------------
# Assignment 2: Adding and Removing Elements
# Add 11 and remove 1.
# -----------------------------------------------------
s.add(11)
s.remove(1)
print(s)


# -----------------------------------------------------
# Assignment 3: Set Operations
# Union, Intersection, Difference, Symmetric Difference
# -----------------------------------------------------
a = set(range(1, 6))
b = {2, 4, 6, 8, 10}

print(a | b)   # Union
print(a & b)   # Intersection
print(a - b)   # Difference
print(a ^ b)   # Symmetric Difference


# -----------------------------------------------------
# Assignment 4: Set Comprehension
# Squares of first 10 positive integers
# -----------------------------------------------------
squares = {x**2 for x in range(1, 11)}
print(squares)


# -----------------------------------------------------
# Assignment 5: Filtering Sets (Even Numbers)
# -----------------------------------------------------
evens = {x for x in s if x % 2 == 0}
print(evens)


# -----------------------------------------------------
# Assignment 6: Removing Duplicates using Set
# -----------------------------------------------------
lst = [1,2,3,4,5,6,5,4,3,2,1]
unique_set = set(lst)
print(unique_set)


# -----------------------------------------------------
# Assignment 7: Subsets and Supersets
# -----------------------------------------------------
set1 = {1,2,3,4,5}
set2 = {1,2,3}

print(set2.issubset(set1))
print(set1.issuperset(set2))


# -----------------------------------------------------
# Assignment 8: Frozenset
# -----------------------------------------------------
fs = frozenset([1,2,3,4,5])
print(fs)


# -----------------------------------------------------
# Assignment 9: Set and List Conversion
# -----------------------------------------------------
my_set = {1,2,3,4,5}
my_list = list(my_set)
my_list.append(6)
my_set = set(my_list)
print(my_set)


# -----------------------------------------------------
# Assignment 10: Set as Dictionary Keys
# -----------------------------------------------------
my_dict = {
    frozenset([1,2,3]): 10,
    frozenset([4,5,6]): 20
}
print(my_dict)


# -----------------------------------------------------
# Assignment 11: Iterating Over Sets
# -----------------------------------------------------
my_set = {1,2,3,4,5}
for element in my_set:
    print(element)


# -----------------------------------------------------
# Assignment 12: Removing Elements Until Empty
# -----------------------------------------------------
my_set = {1,2,3,4,5}
while my_set:
    print("Removed:", my_set.pop())
    print(my_set)


# -----------------------------------------------------
# Assignment 13: Symmetric Difference Update
# -----------------------------------------------------
set1 = {1,2,3}
set2 = {3,4,5}
set1.symmetric_difference_update(set2)
print(set1)


# -----------------------------------------------------
# Assignment 14: Membership Testing
# -----------------------------------------------------
print(3 in set1)
print(10 in set1)


# -----------------------------------------------------
# Assignment 15: Set of Tuples
# -----------------------------------------------------
tuple_set = {(1,2), (3,4), (5,6)}
print(tuple_set)


# =====================================================
# Lesson 3.4: Dictionaries
# =====================================================

# -----------------------------------------------------
# Assignment 1: Creating Dictionary
# -----------------------------------------------------
squares = {i: i**2 for i in range(1, 11)}
print(squares)


# -----------------------------------------------------
# Assignment 2: Accessing Elements
# -----------------------------------------------------
print(squares[5])
print(squares.keys())


# -----------------------------------------------------
# Assignment 3: Dictionary Methods
# -----------------------------------------------------
squares[11] = 121
del squares[1]
print(squares)


# -----------------------------------------------------
# Assignment 4: Iterating Dictionary
# -----------------------------------------------------
for k, v in squares.items():
    print(k, v)


# -----------------------------------------------------
# Assignment 5: Dictionary Comprehension (Cubes)
# -----------------------------------------------------
cubes = {i: i**3 for i in range(1, 11)}
print(cubes)


# -----------------------------------------------------
# Assignment 6: Merging Dictionaries
# -----------------------------------------------------
d1 = {i: i**2 for i in range(1, 6)}
d2 = {i: i**2 for i in range(6, 11)}
merged = d1 | d2
print(merged)


# -----------------------------------------------------
# Assignment 7: Nested Dictionary
# -----------------------------------------------------
student = {
    "name": "Kaif",
    "age": 21,
    "grades": {
        "math": 85,
        "science": 78,
        "english": 90
    }
}
print(student)


# -----------------------------------------------------
# Assignment 8: Dictionary of Lists
# -----------------------------------------------------
multiples = {i: [i*j for j in range(1, 6)] for i in range(1, 6)}
print(multiples)


# -----------------------------------------------------
# Assignment 9: Dictionary of Tuples
# -----------------------------------------------------
square_tuple = {i: (i, i**2) for i in range(1, 6)}
print(square_tuple)


# -----------------------------------------------------
# Assignment 10: Dictionary to List
# -----------------------------------------------------
dict_list = list(square_tuple.items())
print(dict_list)


# -----------------------------------------------------
# Assignment 11: Dictionary Filtering
# -----------------------------------------------------
even_dict = {k:v for k,v in squares.items() if k % 2 == 0}
print(even_dict)


# -----------------------------------------------------
# Assignment 12: Swap Keys and Values
# -----------------------------------------------------
swapped = {v:k for k,v in square_tuple.items()}
print(swapped)


# -----------------------------------------------------
# Assignment 13: Default Dictionary
# -----------------------------------------------------
from collections import defaultdict
dd = defaultdict(list)
dd["a"].append(1)
dd["b"].append(2)
print(dd)


# -----------------------------------------------------
# Assignment 14: Character Count
# -----------------------------------------------------
def char_count(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    return count

print(char_count("python"))


# -----------------------------------------------------
# Assignment 15: Dictionary to JSON
# -----------------------------------------------------
import json
book = {
    "title": "Dream",
    "author": "Kaif",
    "year": 2024,
    "genre": "Programming"
}
json_data = json.dumps(book)
print(json_data)

