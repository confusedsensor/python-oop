#Create a class named MyClass, with a property named x:
class MyClass:
    x = 5

#Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

#Delere the p1 object:
del p1

#Create three objects from the MyClass class:
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
class Person:
    pass