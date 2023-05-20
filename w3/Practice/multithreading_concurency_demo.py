# Multithreaded Python program
import time
from threading import Thread


def print_numbers(n):
    for i in range(1, n):
        print(i)
        time.sleep(1)


threads = list()
n_threads = 10
n = 10
for _ in range(n_threads):
    threads.append(Thread(target=print_numbers, args=(n,)))

startTime = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
endTime = time.time()

print("Time taken", endTime - startTime)