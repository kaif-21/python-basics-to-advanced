# =====================================================
# Module 3: Data Structures Assignments
# Lesson 3.2: Tuples
# =====================================================

# -----------------------------------------------------
# Assignment 1: Creating and Accessing Tuples
# Create a tuple with the first 10 positive integers..
# -----------------------------------------------------
t = tuple(range(1, 11))
print(t)


# -----------------------------------------------------
# Assignment 2: Accessing Tuple Elements
# Print first, middle, and last elements.
# -----------------------------------------------------
print("First:", t[0])
print("Middle:", t[len(t)//2])
print("Last:", t[-1])


# -----------------------------------------------------
# Assignment 3: Tuple Slicing
# Print first three, last three, and elements from index 2 to 5.
# -----------------------------------------------------
print(t[:3])
print(t[-3:])
print(t[2:6])


# -----------------------------------------------------
# Assignment 4: Nested Tuples
# Create 3x3 matrix and access 2nd row, 3rd column.
# -----------------------------------------------------
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(matrix)
print("Element:", matrix[1][2])


# -----------------------------------------------------
# Assignment 5: Tuple Concatenation
# -----------------------------------------------------
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)


# -----------------------------------------------------
# Assignment 6: Tuple Methods
# Count and index of element.
# -----------------------------------------------------
t = (1, 1, 2, 3, 2, 4, 1)
print("Count of 1:", t.count(1))
print("Index of 2:", t.index(2))


# -----------------------------------------------------
# Assignment 7: Unpacking Tuples
# -----------------------------------------------------
t = (1, 2, 3, 4, 5)
a, b, c, d, e = t
print(a, b, c, d, e)


# -----------------------------------------------------
# Assignment 8: Tuple Conversion
# Convert list to tuple.
# -----------------------------------------------------
lst = [1, 2, 3, 4, 5]
t = tuple(lst)
print(t)


# -----------------------------------------------------
# Assignment 9: Tuple of Tuples
# -----------------------------------------------------
t = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(t)


# -----------------------------------------------------
# Assignment 10: Tuple and List
# Convert tuple → list → modify → tuple.
# -----------------------------------------------------
t = (1, 2, 3, 4, 5)
lst = list(t)
lst.append(6)
t = tuple(lst)
print(t)


# -----------------------------------------------------
# Assignment 11: Tuple and String
# -----------------------------------------------------
s = "kaif"
t = tuple(s)
result = "".join(t)
print(result)


# -----------------------------------------------------
# Assignment 12: Tuple and Dictionary
# -----------------------------------------------------
d = {
    (1, 2): 10,
    (3, 4): 20
}
print(d)


# -----------------------------------------------------
# Assignment 13: Nested Tuple Iteration
# -----------------------------------------------------
t = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for inner in t:
    for item in inner:
        print(item)


# -----------------------------------------------------
# Assignment 14: Tuple and Set
# Remove duplicates using set.
# -----------------------------------------------------
t = (1, 1, 2, 2, 3, 4, 5, 5)
s = set(t)
print(s)


# -----------------------------------------------------
# Assignment 15: Tuple Functions
# Min, Max, Sum of tuple.
# -----------------------------------------------------
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)

def tuple_operations(t):
    return min(t), max(t), sum(t)

minimum, maximum, total = tuple_operations(t)
print("Min:", minimum)
print("Max:", maximum)
print("Sum:", total)

