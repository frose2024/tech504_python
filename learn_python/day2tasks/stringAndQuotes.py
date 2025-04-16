"""
bad_string = 'I said 'Wow!''
print(bad_string)
"""
# This fails because of the ' midway through. Python interprets that as the end of the string, and everything past that as nonsense.

# How to make this work?
good_string1 = "I said 'Wow!'"
good_string2 = "\nI said" + ' ' + "'Wow!'"
wow = " 'Wow!'"
good_string3 = "\nI said" + wow
good_string4 = '\nI said \'Wow!\''
print(good_string1, good_string2, good_string3, good_string4)

# What is best practice? Honestly my instinct is to always use " "

# String slicing
Hw = "Hello world!"
print(Hw)

# How many characters does Hw have? Using the string length function, len()
print(len(Hw))

# Get the character in the first position in Hw
print(Hw[0])

# Get the last character - using len first will tell you how long the string's array is, last character will be len - 1
print(Hw[11])

# Get the second to last character
print(Hw[10])

# What does this code do? Prints everything except the first two characters/elements in the array
print(Hw[2:])

# What does this code do? Prints the last three characters in the string/doesn't print anything before the last 3 characters
print(Hw[-3:])

# What does this code do? Omits everything past the first 5 character from the print statement
print(Hw[:5])

# Starts from the second, stops at the fifth
print(Hw[1:4])





