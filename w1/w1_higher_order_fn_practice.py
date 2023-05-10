
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

# Return a function
def f2(c, d):
    return c, d

def f1(a, b):
    c = a + 1
    d = b + 2
    return lambda: f2(c, d)

result = f1(1, 2)
print(result)
print(result())

# Anonymous function
# lambda arguments: expression

# Define a lambda function that returns the square of a number
square = lambda x: x ** 2

# Use the lambda function to calculate the square of 5
result = square(5)

# Print the result
print(result)  # Output: 25

# anonymous function that takes no arguments
# Define a lambda function that returns hello world
hello_world = lambda: 'Hello World'
result = hello_world()
# Print the result
print(result)

# Map, filter and reduce
# Map(): map(mapping_function, *iterables)

# a function to calculate the predicted and actual target values
def squared_difference(x, y):
    predicted_y = 4 * x + 21
    diff = predicted_y - y
    return diff ** 2

values = [{
    'x': 2,
    'y': 26
}, {
    'x': 3,
    'y': 34
}, {
    'x': 4,
    'y': 37
}, {
    'x': 7,
    'y': 61
}]

differences = list(map(squared_difference, [val['x'] for val in values], [val['y'] for val in values]))
print(differences)

# Filter(): filter(filter_function, iterable)
students = {
    'Aaron': {
        'Physics': 95,
        'Chemistry': 80,
        'Math': 92,
    },
    'David': {
        'Physics': 99,
        'Chemistry': 85,
        'Math': 92,
    },
    'John': {
        'Physics': 92,
        'Chemistry': 84,
        'Math': 89,
    },
    'Danny': {
        'Physics': 93,
        'Chemistry': 82,
        'Math': 91,
    },
    'Zach': {
        'Physics': 97,
        'Chemistry': 86,
        'Math': 93,
    },
}


def check_if_student_qualifies(student_details):
    name, scores = student_details
    condition0 = scores['Physics'] > 95
    condition1 = scores['Chemistry'] > 83
    condition2 = scores['Math'] > 90

    return all([condition0, condition1, condition2])


students_tuple = [(name, scores) for name, scores in students.items()]
qualified_students = dict(filter(check_if_student_qualifies, students_tuple))
print(qualified_students)


# Reduce(): reduce(reduce_function, iterable)

from functools import reduce
values = [2, 3, 4, 7, 10, 21]

print(reduce(lambda x, y: x+y, values)) # sum of all values in a list
print(reduce(lambda x, y: x*y, values)) # product of all values in a list







