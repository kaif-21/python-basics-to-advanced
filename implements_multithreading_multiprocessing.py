# real world example
# multithreading
'''
https://www.langchain.com/
'''

import threading
import requests
import bs4

urls = [
    'https://www.langchain.com/'
]

def fetch_content(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All done")

# multiprocessing

import multiprocessing
import time
import sys
import math

# increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# function to compute factorials of a given numbers

def computer_factorial(number):
    print(f"compute a factorial of {number}")
    result = math.factorial(number)
    return result

if __name__ == '__main__':
    numbers=[5000,6000,7000,8000]

    start_time = time.time()

#     create a pool of worker processes
    with multiprocessing.Pool() as pool:
        result = pool.map(computer_factorial, numbers)

    end_time = time.time()
    print(f"result: {result}")
    print(f"time taken : {end_time-start_time}seconds")
