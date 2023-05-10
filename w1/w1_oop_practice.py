
class LineItem:
    # Constructor method to initialize the instance attributes
    def __init__(self, stock_code, product_description, unit_price, quantity, date):
        self.stock_code = stock_code
        self.product_description = product_description
        self.unit_price = unit_price
        self.quantity = quantity
        self.date = date

    # Method to print the car's details
    def print_details(self):
        print("Stock Code:", self.stock_code)
        print("Product Description:", self.product_description)
        print("Unit Price:", self.unit_price)
        print("Quantity:", self.quantity)
        print("Date:", self.date)


# Creating object instances of the Car class
line_item1 = LineItem(stock_code="82095", product_description="HEART BUTTONS JEWELLERY BOX",
                      unit_price=4.96, quantity=1, date="2015/04/06")
line_item2 = LineItem(stock_code="21070", product_description="VINTAGE BILLBOARD MUG",
                      unit_price=2.46, quantity=1, date="2015/10/15")


# Printing the details of the car instances
line_item1.print_details()
print("\n")
line_item2.print_details()

# modify the stock_code attribute
line_item1.stock_code = "82099"
# access the unit_price attribute
print(line_item1.unit_price)

# Methods

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area = None

    def calculate_area(self):
        self.area = self.length * self.breadth

study_room = Rectangle(length=10, breadth=20)
study_room.calculate_area()
study_room.area

# Constructors

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(1,2)

# Inheritance

class Product:
    def __init__(self, price, stock_code, unit_price):
        self.stock_code = stock_code
        self.price = price
        self.unit_price = unit_price
        
    def product_description(self):
        return None
    
class NikeMercurial(Product):
    def __init__(self, price, stock_code, unit_price, description):
        super().__init__(price, stock_code, unit_price)
        self.description = description
    
    def product_description(self):
        return self.description

prod = NikeMercurial(price=100, stock_code="1234", unit_price=50, description="Nike Mercurial")

prod.description

# Multiple Inheritance
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print("Hello, my name is", self.name)

class Athlete:
    def __init__(self, sport):
        self.sport = sport
    
    def play(self):
        print("I play", self.sport)

class SportsPerson(Person, Athlete):
    def __init__(self, name, sport):
        Person.__init__(self, name)
        Athlete.__init__(self, sport)
        
my_sportsperson = SportsPerson("Kylian Mbappe", "Football")
my_sportsperson.greet() # prints "Hello, my name is Kylian Mbappe"
my_sportsperson.play() # prints "I play Football"

# Method Resolution Order in Multiple Inheritance

class A:
    def foo(self):
        print("A.foo")

class B(A):
    def foo(self):
        print("B.foo")
        super().foo()

class C(A):
    def foo(self):
        print("C.foo")
        super().foo()

class D(B, C):
    def foo(self):
        print("D.foo")
        super().foo()

d = D()
d.foo()

b = B()
b.foo()

c = C()
c.foo()

# Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")
    
    def get_balance(self):
        return self.__balance

my_account = BankAccount(1000)
my_account.deposit(500)
my_account.withdraw(200)
print(my_account.get_balance()) # prints 1300

# Polymorphism

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Rectangle(5, 10), Circle(7), Triangle(8, 12)]

for shape in shapes:
    print(shape.area())
    
# Polymorphism in action using os module

import os

# Open a text file and write some text to it
with open("my_text_file.txt", "w") as f:
    f.write("Hello, world!")

# Open a text file and append some text to it
with open("my_text_file.txt", "a") as f:
    f.write("Some more data")

# Open a text file and read data from it
with open("my_text_file.txt", "r") as f:
    print(f.read())

# Open a binary file and read some data from it

with open("my_binary_file.bin", "w") as f:
    f.write(str(1024))

with open("my_binary_file.bin", "rb") as f:
    data = f.read()
    

# @classmethod 

