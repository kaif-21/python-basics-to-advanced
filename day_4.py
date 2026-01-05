# Day 4: Data Structures - Tuple

# ---------------------------------
# Creating Tuples
empty_tuple = tuple()
print("Empty tuple:", empty_tuple)
print("Type:", type(empty_tuple))

mixed_tuple = (1, "hello world", 3.45, True)
print("Mixed tuple:", mixed_tuple)

# ---------------------------------
# Accessing Tuple Elements
numbers = (1, 2, 3, 4, 5, 6)
print("Element at index 4:", numbers[4])
print("Slice [2:4]:", numbers[2:4])

# ---------------------------------
# Tuple Operations
concat_tuple = mixed_tuple + numbers
print("Concatenated tuple:", concat_tuple)

print("Tuple repetition:", mixed_tuple * 2)

# ---------------------------------
# Immutability of Tuple
# Tuples are immutable (cannot be modified)

sample_list = [1, 2, 3, 4]
sample_list[1] = "kaif"
print("List is mutable:", sample_list)

# numbers[1] = 10  ❌ This will give an error

# ---------------------------------
# Tuple Methods
repeated_numbers = (1, 1, 2, 3, 1, 4, 1, 5, 1)
print("Count of 1:", repeated_numbers.count(1))
print("Index of 3:", repeated_numbers.index(3))

# ---------------------------------
# Packing and Unpacking Tuple
packed_tuple = 10, "Python", 3.14
print("Packed tuple:", packed_tuple)

a, b, c = packed_tuple
print(a)
print(b)
print(c)

# ---------------------------------
# Unpacking with *
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *middle, last = numbers_list
print("First:", first)
print("Middle:", middle)
print("Last:", last)

# ---------------------------------
# Nested Tuple
nested_tuple = (
    (1, 2, 3),
    ("a", "b", "c"),
    (True, False)
)

print("First tuple:", nested_tuple[0])
print("Third tuple:", nested_tuple[2])

# ---------------------------------
# Iterating Over Nested Tuple
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item, end=" ")
    print()

# ---------------------------------
# End of Day 4



