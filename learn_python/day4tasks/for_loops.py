# for loops in python will execute a given statement/statements once for each item in the loop.

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# 1. - write a loop that prints each number in the list_Data
for num in list_data:
    print(num * 2)


# 2. - loop through the embedded list.
for data in embedded_lists:
    print(data)


# 3. - loop through the list within a list (nested)
for data in embedded_lists:
    print(data)
    for more_data in data:
        print(more_data)


# 4. - loop through a dictionary
for information in dict_data:
    print(information)


"""
5. - loop through a dictionary and print the key-value pairs
    Was confused here also, but "for val dict_data.values()" is applying the values.() method to each inner dictionary in the dictionary
    .values() gets all of the key-values pairs for a dictionary. By using a for loop we're saying 'for each dictionary in dict_data,
    apply the .values() method to each one"
"""
for val in dict_data.values():
    print(val)


# 6. - Generate an embedded for loop (a loop within a loop) to extract and print the values within the dictionary of each item in the dictionary
#   Also took me a second to understand, but here we're using the first loop to get each dictionary from dict_data with .values
#   And then using .values on each individual dictionary item to retrieve item from each dictionary and print them
#   each dictionary item is represented by "values". So when we print 'values' we're printing each value
for val in dict_data.values():
    for values in val.values():
        print(values)


# 7. - loop through to print specific values of the dictionary items inside a dictionary
#   Got confused here too. Lot of confusion today, but my issue was going too many loops deep.
#   for each 'val' (each inner dictionary) we're using .get to retrieve the value from each key "money"
for val in dict_data.values():
    x = val.get("money")
    print(x)


# 8. - loop through a list with a nested if statement
for value in list_data:
    if value < 3:
        print("less than 3")
    elif value == 3:
        print("I found 3")
    elif value > 3:
        print("greater than 3")