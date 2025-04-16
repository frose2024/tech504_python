name = "Lassie"
years = 7
height_cm = 60.2

# Print these variables in an f-string so that it outputs "Lassie is 7 years old and 60.2cm tall"
# It's string interpolation in JS bois.

print(f"{name} is {years} years old and {height_cm}cm tall.")


pi = 3.14159265359
# Use an f-string to print pi to 3 decimal places
print(f"Pi to 3 decimal places: {pi:.3f}")

# Use an f-string to print pi to 5 decimal places
print(f"Pi to 3 decimal places: {pi:.5f}")

score = 16
max_score = 26
score_as_decimal = score/max_score
# Use an f-string to print 'score as decimal;
print(f"You scored {score_as_decimal}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage and rounded to 2 decimal places.
print(f"You scored {score_as_decimal * 100:.2f}%")

# Use an f-string to print 'score_as_decimal' formatted as a percentage to a rounded whole number
# Can use the round() function to achieve this
rounded_score = round(score_as_decimal * 100)
print(f"You scored {rounded_score}%")



