# multithreading with thread pool executor
from concurrent.futures import ThreadPoolExecutor

import time
def print_numbers(numbers):
    time.sleep(1)
    return f"numbers: {numbers}"

numbers = [1,2,3,4,5,6,7,8,9,87,76,65,5,65]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, numbers)

for result in results:
    print(result)

# multiprocessing with processpoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"square: {number * number}"

numbers = [1,2,3,4,5,6,7,8,9,87,76,65,5,65]
if __name__ == '__main__':

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)
    for result in results:
            print(result)