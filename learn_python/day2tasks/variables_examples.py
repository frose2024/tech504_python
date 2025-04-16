# What is a variable? A stored data location

# Why is it called a variable? Because it can vary, i.e it can be altered.

# Setting a variable with a number value
a = 45

# Setting a variable with a float
b = 45.5

# Setting a variable with a string
c = 'Isaac'

# How is using '==' different? It's an equality operator, will return a boolean saying if the two values are equal or not.

print(a, type (a), b, type (b), c, type (c))



""""
# What does it mean that Python is a strongly typed language? Variables have a type, that type determines what operations can be performed on them.
# Weakly typed language could be JS - it allows for conversion btwn data types.
    "some string" - 3
"""


""" 
What does it mean that Python is a dynamically typed language? Variable types are determined and checked at runtime, not compilation, so their type can change mid-program.
Statically typed language could be C - will break your code if you accidentally re-assign a variable.
"""
x = 10
print(x)
x = 'Kyle'
print(x)


# id is a python function, will return the 'identity' of an object.
frog = 77
print(id(frog))
frog = 78
print(id(frog))
# Why does the id change? The id of an object is its location in memory when that object is created. Altering that variable = re-creating it.


# Assign one variable to another
x = 10
y = x
print(id(x), id(y))
# The id is the same because y is pointing to x.
x = 9
print(id(x), id(y))
y = x
# when y was created it pointed to the value of old x. y hasn't been updated since then, it's still pointing to the same thing.
print(id(x), id(y))
# now y has been updated, it's pointing to the new x.


# Ask for user input and print it to the screen. User input done with the input() method.
username = input("Enter username: ")
print("Username is: " + username)
# Syntax wise, the input method has been applied to the 'username' variable. Once the input is received, the username
# variable is assigned the value of that input.
age = input("How old are you? ")
DOB = input("When were you born? ")
print("Hello " + username + ".\nYou look old for " + age + ".")


# Improved edition of the above code.
# What is your name - asking for user input, save as a variable.
name = input("What is your name? ")
# What is your age?
age = input("What is your age? ")
int_age = int(age)
# What month were you born?
month = input("What month were you born in? ")
# What year were you born?
year = input("What year were you born in? ")
# Final print statement putting all the user input together.
print("Hi " + name + ", " + str(age))
print(f"You were born in {month} of the year {year}")
