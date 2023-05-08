
# Store a function in a variable
def func(arg):
    return arg**2

func_ref = func
print(func_ref(2))

# Pass a function as a parameter to another function
def evaluate(f, start, end):
    nums = [num for num in range(start, end) if num % 2 == 0] # choosing even numbers
    return f(nums)

def generate_squares(values):
    return [value**2 for value in values]

def generate_cubes(values):
    return [value**3 for value in values]

print(evaluate(f=generate_squares, start=0, end=10))
print(evaluate(f=generate_cubes, start=0, end=10))

# A callback is a function that is passed as an argument to another function and 
# can run after the main function has been completed
