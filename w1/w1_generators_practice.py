import random
import uuid
from pprint import pprint
import sys

# helper function that returns sample sales data in batches
def generate_batch_data(n_batch=100, n_per_batch=5):
  for _ in range(n_batch):
    batch_data = []
    for _ in range(n_per_batch):
      country = random.choices(['United States', 'China', 'Japan', 'Germany', 'India',
                                'United Kingdom', 'France', 'Canada', 'Russia', 'Italy'],
                              [0.2, 0.05, 0.05, 0.1, 0.1, 0.2, 0.1, 0.1, 0.05, 0.05])
      
      description = random.choices(["CREAM CUPID HEARTS COAT HANGER", "CREAM HANGING HEART T-LIGHT HOLDER", "POPPY'S PLAYHOUSE BEDROOM ", 
                                    "FELTCRAFT PRINCESS CHARLOTTE DOLL", "IVORY KNITTED MUG COSY", "DOORMAT NEW ENGLAND", "YELLOW COAT RACK PARIS FASHION", 
                                    "SPACEBOY LUNCH BOX", "ALARM CLOCK BAKELIKE GREEN", "PANDA AND BUNNIES STICKER SHEET"],
                              [0.2, 0.05, 0.05, 0.1, 0.1, 0.2, 0.1, 0.1, 0.05, 0.05])
      
      batch_data.append({
          'StockCode': str(uuid.uuid4()),
          'Description': description[0],
          'UnitPrice': random.uniform(0.01, 10),
          'Country': country[0],
          'InvoiceNo': str(uuid.uuid1())
      })
    
    yield batch_data

batch_generator = generate_batch_data()
for batch in batch_generator:
  pprint(batch)
  print("\n")
  
# Example 2
def even_numbers(n):
    for i in range(n):
        yield 2*i

# Example usage
for num in even_numbers(5):
    print(num)
    
# Example 3
def generate_numbers(end, start=0):
  value = start
  while value < end:
    yield value
    value += 1
  
number_generator = generate_numbers(start=5, end=10)
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))
print(next(number_generator, None))

# Example 4

import os
cwd = os.getcwd()
print(cwd)


def csv_reader(file_name):
  for row in open(file_name, 'r'):
    yield row

csv_gen = csv_reader("MLTollsStackOverflow.csv")
row_count = 0

for row in csv_gen:
  row_count += 1

print(f"Row count is : {row_count}")