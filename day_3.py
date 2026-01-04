# Day 3: Data Structures - List & List Comprehension

# ---------------------------------
# Creating a List
lst = []
print(type(lst))

fruits = ['apple', 'banana', 'orange', 'kiwi', 'mango', 'pineapple']
print("Fruits list:", fruits)

# ---------------------------------
# Accessing List Elements (Slicing)
print("Slice [1:5]:", fruits[1:5])
print("Slice [1:]:", fruits[1:])
print("Last element:", fruits[-1])

# ---------------------------------
# Modifying List Elements
fruits[1] = "watermelon"
print("After modification:", fruits)

# ---------------------------------
# List Methods
fruits.append("kaif")
print("After append:", fruits)

fruits.insert(0, "danish")
print("After insert:", fruits)

fruits.remove("orange")
print("After remove:", fruits)

index = fruits.index("kaif")
print("Index of kaif:", index)

fruits.sort()
print("Sorted list:", fruits)

fruits.reverse()
print("Reversed list:", fruits)

# ---------------------------------
# List Slicing with Numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
print("numbers[1:6]:", numbers[1:6])
print("numbers[:6]:", numbers[:6])
print("numbers[::2]:", numbers[::2])
print("numbers[::-1]:", numbers[::-1])

# ---------------------------------
# Iterating Over a List
for num in numbers:
    print(num)

print("Using enumerate:")
for index, num in enumerate(numbers):
    print(index, num)

# ---------------------------------
# List Comprehension
squares = [x ** 2 for x in range(10)]
print("Squares:", squares)

table_of_9 = [x * 9 for x in range(11)]
print("Table of 9:", table_of_9)

# ---------------------------------
# End of Day 3


