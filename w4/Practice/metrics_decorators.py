def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function
def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)

## Metrics decorators

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@timer_decorator
def my_function(a,b):
    return a + b


# Execution time metric decorator
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds to run")
        return result
    return wrapper

@timeit
def my_func():
    for _ in range(10000000):
        pass

my_func()

# track number of calls
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@count_calls
def my_func():
    # some code here
    pass

for _ in range(10):
    my_func()

print(my_func.count)  # prints 10