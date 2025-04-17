# 1. Function with no argument
def print_something():
    print("print something")

print_something()

# Function that takes an argument
def print_something_better(something):
    print(something)

print_something_better("kyle")


# Function that makes a more interesting version that accepts one
def greet(name:str):
    x = name
    print("Hello, my name is " + x)

greet("Susan")


# Function w/ 2 arguments that returns a value
def addition(int1, int2):
    x = int1 + int2
    print(x)

addition(2, 2)
# Answer i

# Make a function w/ default values - default values in python = assigning the argument values as a fallback if nothing is passed.
def addition(int1 = 2, int2 = 2):
    return int1 + int2

print(addition())

print(addition(4, 4))
# Answer is now 4 b/c default are used when nothing else is passed/passed arguments overwrite default values.

# Make a function that accepts any number of arguments
def print_any_number(a_tuple):
    print(type(a_tuple))
    for x in a_tuple:
        print(x)

print_any_number((7, 9, 9))

# What character allows a function to accept multiple arguments? * = it tells the function to take all the given arguments
#   put them into a tuple.
def print_any_number(*a_tuple):
    print(type(a_tuple))
    for x in a_tuple:
        print(x)

print_any_number(7, 9, 9)


# Make a function which gives a hint about an argument's data type - using :<type> gives a hint as to the argument's data type.
def greet(name:str):
    x = name
    print("Hello, my name is " + x)

# Below code won't work because the function is expecting a string
#   greet(24602)



# Make a function which gives a hint about a return value's data type
def division(int1:int = 2, int2:int = 5) -> float:
    return int1 / int2

print(division())

a = 4
b = 6
print(division(a, b))


# What are some good practices when it comes to functions? Simple names that explain what they do.