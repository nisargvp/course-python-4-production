import threading
import time

def worker():
    print("Starting worker thread")
    time.sleep(2) # simulate some work
    print("Exiting worker thread")
    
t = threading.Thread(target=worker)
t.start() 

print("Main thread waiting for worker thread to finish")
t.join() # wait until the worker thread finishes
print("Main thread exiting")