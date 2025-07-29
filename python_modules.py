"""
    A module in Python is simply a Python file that contains definitions and statements. 
    It can define functions, classes, and variables that you can reference in other Python files, or scripts, using the 'import' statement
    Here's an example of how you can create your own Python module:
"""

# (1) create a python file
# mymodule.py - in this file, we've defined two functions: 'greet' and 'add_numbers'
def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

# (2) use the module - you can use these functions in another Python file by importing the module
# main.py - in this file, we import 'mymodule' and then call the functions defined in 'mymodule.py'
import mymodule

print(mymodule.greet("Alice"))  # prints: Hello, Alice!
print(mymodule.add_numbers(1, 2))  # prints: 3

# example module - datetime
# the 'datetime' module supplies classes for manipulating dates and times
import datetime
now = datetime.datetime.now()   # Get the current date and time
print(f"Current date and time: {now}")
current_time = now.time()       # Get just the current time
print(f"Current time: {current_time}")

# example module - os
# the 'os' module provides a way of using operating system dependent functionality
import os
cwd = os.getcwd()       # Get the current working directory
print(f"Current working directory: {cwd}")
print("Files and directories:", os.listdir(cwd))    # List all files and directories in the current directory

# example module - random
# the random module can generate random numbers
import random
random_number = random.randint(1, 10)   # Generate a random number between 1 and 10
print(f"Random number between 1 and 10: {random_number}")
my_list = ['apple', 'banana', 'cherry'] # Randomly select an item from a list
random_item = random.choice(my_list)
print(f"Random item from list: {random_item}")

