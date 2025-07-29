print("Hello, World!")

# defining a function
# in this example, 'greet' is a function with only one parameter and prints a greeting
def greet(name):
    print(f"Hello, {name}!")

# calling a function 
# to call a function you use its name followed by parenthesis, and if the function requires parameters, you pass them inside them
greet("Alice")

# return values
# allows you to get a result from a function and use it elsewhere in your code
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# parameters and arguments
# parameters are the variables listed inside parenthesis in the function definition
# arguments are the values you pass to the function when you call it
def multiply(x, y): 
    return x * y

print(multiply(4, 5))

# default parameters
# if an argument if not provided, the default value is used
def greeting(name = "World"): 
    print(f"Hello, {name}!")

greeting()
greeting("Alice")

# keyword arguments
# you can call functions using keyword arguments where you specify the parameter name along with its value
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Buddy")
describe_pet(pet_name="Whiskers", animal_type="cat")

# arbituary arguments
# if you don't know how many arguments will be passed to your function, you can use '*args' for positional arguments and '**kwargs' for keyword arguments
def make_pizza(*toppings):
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni", "mushrooms", "green peppers")

# arbituary arguments continued
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# object oriented design
# programming paradigm that uses "objects" to model real-world entities
# these objects are instances of "classes," which can be thought of as blueprints for creating objects

# object oriented design (1) - class vs object
# class: defines a set of attributes and methods that the objects created from the class will have
# object: represents a specific entity with attributes and behaviors defined by the class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
    
my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.bark())

# object oriented design (2) - encapsulation 
# encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, or class
class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

my_car = Car("Toyota", "Corolla")
print(my_car.get_make())  # Output: Toyota

# object oriented design (3) - inheritance
# inheritance allows a class to inherit attributes and methods from another class
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
my_dog = Dog()
my_cat = Cat()
print(my_dog.speak())
print(my_cat.speak())

# object oriented design (4) - polymorphism
# allows methods to do different things based on the object it is acting upon
class Bird:
    def fly(self):
        return "Flying high!"

class Penguin(Bird):
    def fly(self):
        return "I can't fly!"

my_bird = Bird()
my_penguin = Penguin()
print(my_bird.fly())  # Output: Flying high!
print(my_penguin.fly())  # Output: I can't fly!

# object oriented design (5) - abstraction
#  means hiding the complex implementation details and showing only the essential features of the object
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

my_rectangle = Rectangle(3, 4)
print(my_rectangle.area())

# working with file
"""
    # opening and closing files
    # Always remember to close the file after you are done to free up system resources
    # Open a file for reading, do something with file, then close the file
    file = open("example.txt", "r")
    content = file.read()
    print(content)
    file.close()

    # using the 'with' statement
    # ensures that the file is properly closed after its suite finishes, even if an exception is raised
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)  # No need to explicitly close the file

    # reading files (1) - reading the entire file
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

    # reading files (2) - read line by line 
    with open("example.txt", "r") as file:
        for line in file:
            print(line.strip())

    # reading files (3) - read into a list
    with open("example.txt", "r") as file:
        lines = file.readlines()
            print(lines)

    # writing to files
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a new line.")

    # appending to files
    with open("example.txt", "a") as file:
        file.write("\nThis line is appended.")

    # working with binary files
    with open("example.jpg", "rb") as file:
        content = file.read()
        print(content)

    with open("copy.jpg", "wb") as file:
        file.write(content)

    # handling file exceptions
    try:
        with open("nonexistent.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("The file does not exist.")

    # using the 'os' and 'pathlib' modules (1) - listing files in a directory
    import os
    print(os.listdir("."))
    
    # using the 'os' and 'pathlib' modules (2) - creating directories
    os.mkdir("new_directory")
    
    # using the 'os' and 'pathlib' modules (3) - using 'pathlib' for path manipulations
    from pathlib import Path
    path = Path("example.txt")
    print(path.exists())
    print(path.is_file())
    print(path.parent)
"""

