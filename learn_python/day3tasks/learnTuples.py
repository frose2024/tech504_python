"""
How are tuples similar to lists?
  Tuples are also used to multiple items in a single variable.

Are tuples immutable?
  Yes, once they've been created they cannot be changed. Cannot add/change/remove items to it.

What other data types are immutable?
  Numbers, booleans, strings. Majority of built-in data types.
  You can still reassign (some of) them, but when you do that you're destroying the old version and creating a new one.

What are good use cases for tuples instead of lists?
  If you know that you don't want the data stored to ever be altered.

Ohhhh, is tuple just a mispelt abbreviation of immutable?
"""

essentials = ("bread", "eggs", "milk")
print(essentials.count("bread"))
# This code creates a tuple (uses braces, not square brackets) on l18, then tells you how many times 'bread' appears



# Stranded on a Desert IsLand Game
print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")

# Save the items as a tuple
essentials_tuple = (essential_item1, essential_item2, essential_item3)

# Print the tuple
print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")

"""
Try to add the 4th item to the tuple
Doesn't work - essentials_tuple.append(essential_item4)
If you can't add the 4th item, work out how to save the 4th item to the tuple
"""

# We have a three stage approach here :

# 1 - turn tuple into list via casting
essential_list = list(essentials_tuple)
print(essential_list)

# 2 - append new item
essential_list.append(essential_item4)
print(essential_list)

# 3 - turn back into tuple via casting
essentials_tuple = tuple(essential_list)

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)
