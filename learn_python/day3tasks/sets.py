"""
How are sets different to lists and tuples?
    Sets are unordered (dictionaries are ordered)
    Sets are mutable (tuples are immutable). You can't change items, but you can add + remove.
    Sets do not duplicate members
    Sets use { }, tuples use ( ) and dictionaries also use { } but with key-value pairs as well.
"""

fruits = {"apple", "banana", "cherry"}
print(fruits)
# Each print execution has a different order (hence the unordered-ness)

# Add items to a set using the add() method
fruits.add("orange")
print(fruits)

# Remove items from a set using the remove() method
fruits.remove("banana")
print(fruits)

# If I try to add another apple to the set, it won't work. Any copies will be ignored.
fruits.add("apple")
print(fruits)

""" 
Print the 2nd item in the set?
    print(fruits[1]) doesn't work because sets don't allow access via index/key. 
    Workarounds include - using a loop, or the in keyword
"""
x = "apple"
for x in fruits:
        print(x)
# This will print everything in the set, which will include "apple"
# Using the in keyword (could use not in too) will confirm if something is in a set.
print("apple" in fruits)

# Other solution could be to cast the set into a list, and access apple that way. But, set is unordered, so you
#   don't know where exactly apple will end up. 