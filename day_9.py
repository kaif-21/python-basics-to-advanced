"""
Python Modules and Standard Library Demo
Author: Kaif
Purpose: Learning how to use modules, packages, and standard libraries in Python
"""

# =========================
# USER DEFINED FUNCTION
# =========================

def multiply(a, b):
    return a * b


# =========================
# MATH & NUMPY MODULES
# =========================

import math
import numpy as np

print("Square root of 24:", math.sqrt(24))
print("Value of PI:", math.pi)
print("Numpy Array:", np.array([1, 23, 4]))


# =========================
# ARRAY MODULE
# =========================

import array

arr = array.array('i', [1, 2, 3, 4, 5])
print("Array:", arr)


# =========================
# RANDOM MODULE
# =========================

import random

print("Random Number:", random.randint(1, 10))
print("Random Fruit:", random.choice(["apple", "banana", "orange"]))


# =========================
# OS MODULE
# =========================

import os

print("Current Working Directory:", os.getcwd())


# =========================
# JSON (DATA SERIALIZATION)
# =========================

import json

data = {"name": "Kaif", "age": 21}

json_str = json.dumps(data)
print("JSON String:", json_str)

parsed_data = json.loads(json_str)
print("Parsed JSON:", parsed_data)


# =========================
# CSV FILE HANDLING
# =========================

import csv

with open("example.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Kaif", 21])

with open("example.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("CSV Row:", row)


# =========================
# DATE & TIME
# =========================

from datetime import datetime, timedelta

now = datetime.now()
yesterday = now - timedelta(days=1)

print("Current Time:", now)
print("Yesterday:", yesterday)


# =========================
# TIME MODULE
# =========================

import time

start_time = time.time()
time.sleep(2)
end_time = time.time()

print("Time Difference:", end_time - start_time)


# =========================
# REGULAR EXPRESSION
# =========================

import re

text = "there are 123 apples"
pattern = r'\d+'

match = re.search(pattern, text)
print("Regex Match:", match.group())


# =========================
# FUNCTION CALL
# =========================

print("Multiply Result:", multiply(2, 3))
