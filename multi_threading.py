# multithreading
# when to use multithreading
# concurrent execution: when you want to improve the throughput of your application by performing multiple operation concurrently

import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(1)
        print(f"letter:{letter}")

# create 2 threads
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)

t=time.time()
# start the thread
t1.start()
t2.start()

# wait for the thread complete
t1.join()
t2.join()
finished_time = time.time()-t
print(finished_time)