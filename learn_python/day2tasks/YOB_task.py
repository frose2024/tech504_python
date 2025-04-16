from datetime import date
from datetime import datetime

"""
First Part - define variables age_int and name_str
    make a calculation as to the year they were born in.
    Print statement

age_int = 5
name_str = "Kyle"
year_born = 2025 - age_int
print(f"OMG, you are {age_int} years old so you were born in {year_born}.")
"""

# Second Part - prompt user for inputs and assign variables
age_int = input("How old are you? ")
age_int = int(age_int)
# print(type(age_int))
name_str = input("What's your name? ")
year_born = 2025 - age_int
print(f"OMG {name_str}, you are {age_int} years old so you were born in {year_born}.")

# Third part - calculate and print out total number of hours this person has lived
hours_lived = age_int * 8760
print(f"That means you have lived {hours_lived} hours.")


# Bonus part - figure out if the person's birthday has already happened this year or not.
# Need to ask user for birthday, save that as variable.
present = date.today()
print(present)
# My confusion here comes from how I would format the user input correctly so that it can be compared to the present.
bday = input("What's your birthday (dd-mm)? ")
print(bday)
bday_object = datetime.strptime(bday, "%d.%m")
print(bday_object)
bday_object < datetime.now()
# My instinct here is to an if/else statement but we haven't covered how to do that in Python yet.