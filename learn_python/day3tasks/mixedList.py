age_int = input("How old are you? ")
age_int = int(age_int)
# print(type(age_int))
name_str = input("What's your name? ")
year_born = 2025 - age_int
print(f"OMG {name_str}, you are {age_int} years old so you were born in {year_born}.")

# Storing the user information in a list.
user_details_list = [age_int, name_str, year_born]
print(user_details_list)

# Checking that age has been saved as an integer (I casted it on line 2)
print(type(user_details_list[0]))

# Asking the user to input their height in cm
height = input("How tall are you in cm? ")

# Casting the height to a float.
height = float(height)

# Appending their height value onto the list
user_details_list.append(height)

print(user_details_list[3])