# List comprehensions
# newlist = [expression(item) for item in iterable if condition]

# example 1
input_list = ['LARGE WHITE HEART OF WICKER', 'SET OF 4 POLKADOT COASTERS', 'MEDIUM CERAMIC TOP STORAGE JAR', 'POLKADOT JAR', 'RED T-SHIRT']
output_list = [sentence for sentence in input_list if len(sentence.split()) <= 2]
print(output_list)

# example 2
input_list = [[1,2], [3,4], [5,6,7], [8,9]]

flattened_list = [item for sublist in input_list for item in sublist]
print(flattened_list)

# Dictionary comprehensions
input_list = ['LARGE WHITE HEART OF WICKER', 'SET OF 4 POLKADOT COASTERS', 'MEDIUM CERAMIC TOP STORAGE JAR', 'POLKADOT JAR', 'RED T-SHIRT']
output_dict = {sentence: len(sentence.split()) for sentence in input_list}
print(output_dict)

# Set comprehensions
input_list = ['LARGE WHITE HEART OF WICKER', 'MEDIUM CERAMIC TOP STORAGE JAR', 'POLKADOT JAR', 'RED T-SHIRT', 'Red T-shirt']
output_set = {sentence.lower() for sentence in input_list}
print(output_set)

# Generator comprehensions
# create a generator object
generator_exp = (num for num in range(0, 10))
print(generator_exp)

for i in generator_exp:
    print(i)
