# Create a class named Person, and use the __init__() function to assign values for name, age, city, and country when an object of the class is created:
class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country 


p1 = Person("John", 36, "New York", "USA")
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
