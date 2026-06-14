# Access multiple properties with self

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.model} {self.year}")

car1 = Car("Toyota","Corolla",2026)
car1.display_info()

# Call one method from another method using self:

class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name
    
    def welcome(self):
        print(self.greet() + "! Welcome to the my repository.")

p1 = Person("John")
p1.welcome()