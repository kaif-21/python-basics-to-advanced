# Day 5: Data Structures - Set

"""
Sets are built-in data types in Python used to store a collection of unique elements.
They are unordered, mutable, and do not allow duplicate values.
Sets are useful for membership testing and mathematical operations.
"""

# ---------------------------------
# Creating Sets
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("My set:", my_set)
print("Type:", type(my_set))

# Empty set (correct way)
empty_set = set()
print("Empty set:", empty_set)

# ---------------------------------
# Adding and Removing Elements
my_set.add(22)
print("After adding 22:", my_set)

my_set.remove(22)
print("After removing 22:", my_set)

# Pop (removes random element)
removed_element = my_set.pop()
print("Removed element:", removed_element)
print("Set after pop:", my_set)

# Clear all elements
my_set.clear()
print("After clear:", my_set)

# ---------------------------------
# Membership Test
my_set = {1, 2, 3, 4, 5}
print("Is 3 in set?", 3 in my_set)
print("Is 10 in set?", 10 in my_set)

# ---------------------------------
# Mathematical Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 66}

# Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference (set1 - set2):", set1.difference(set2))

# Symmetric Difference
print("Symmetric Difference:", set1.symmetric_difference(set2))

# ---------------------------------
# Set Methods
print("Is set1 subset of set2?", set1.issubset(set2))
print("Is set1 superset of set2?", set1.issuperset(set2))

# ---------------------------------
# Removing Duplicates Using Set
lst = [1, 2, 3, 4, 4, 4, 6]
unique_list = set(lst)
print("Unique elements:", unique_list)

# ---------------------------------
# Counting Unique Words in a Text
text = "my name is kaif chouhan and i am from rajasthan in sikar district"
words = text.split()

unique_words = set(words)
print("Unique words:", unique_words)
print("Total unique words:", len(unique_words))

# ---------------------------------
# End of Day 5


### ✅ Day 5: Set
# Topics covered:
# - Creating sets
# - Adding and removing elements
# - Membership testing
# - Set operations (union, intersection, difference, symmetric difference)
# - Subset and superset
# - Removing duplicates using set
# - Counting unique words in text
