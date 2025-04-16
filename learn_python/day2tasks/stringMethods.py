str_with_extra_spaces = "    extra spaces at the start and end   "

# This prints the length of the string variable str_with_extra_spaces
print(len(str_with_extra_spaces))

# Python has the strip() method to remove whitespace. Will now print the length - whitespace
print(len(str_with_extra_spaces.strip()))

example_text = "here's some text with some words of text"
# How many times does 'text' occur in the above variable? Using count() method
text = example_text.count("text")
print(text)

# .lower() method converts string to lowercase
print(example_text.lower())

# .upper() method converts string to uppercase
print(example_text.upper())

# .capitalize() method capitalises the first word in a string
print(example_text.capitalize())

# .replace() method replaces argument a with argument b
print(example_text.replace("with", ","))