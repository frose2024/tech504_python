story1 = {
    "start" : "Once upon a time there was a really cool dragon",
    "middle" : "The dragon's name was Kevin, and I really cannot stress this enough, he was very cool",
    "end" : "Kevin had a long and a happy life."
}

# Print the dictionary
print(story1)

# Print the type
print(type(story1))

# Print only the keys
keys = story1.keys()
print(keys)

# Print only the values
values = story1.values()
print(values)

# Adding a new key-value pair, character
story1["character"] = "Kevin"
print(story1)
