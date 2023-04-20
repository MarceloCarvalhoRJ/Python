
class book:
    def __init__(self):
        self.title = 'Python for Everyone'
        self.author = 'Charles R. Severance'
        self.pages = 260

book.instance = book()
print(book.instance.title)
print(book.instance.author)
print(book.instance.pages)

'''class Car:
    def __init__():
        self.color = "Red" # ends up on the object
        make = "Mercedes" # becomes a local variable in the constructor

car = Car()
print(car.color) # "Red"
print(car.make) # would result in an error, `make` does not exist on the object'''