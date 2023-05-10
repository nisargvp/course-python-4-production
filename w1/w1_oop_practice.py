
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

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y



