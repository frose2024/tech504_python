shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

# Printing the entire list + the list's data type
print(shopping_list, type(shopping_list))

# Printing first item in the list.
print(shopping_list[0])

# Printing last item in the list.
print(shopping_list[-1:])

# Change second item in the list to 'rice' and print.
print(shopping_list[1])
shopping_list[1] = "rice"
print(shopping_list[1])

# Add 'carrots' to the list and then check length. Done using the append() method
print(len(shopping_list))
shopping_list.append("carrots")
print(len(shopping_list))

# Add a second list containing 'toffee' and 'coffee' to shopping_list
shopping_list.append(["toffee", "coffee"])
print(shopping_list)

# Remove 'bananas' from the shopping list. Done using the remove method.
shopping_list.remove("bananas")
print(shopping_list)

# Remove 'coffee' from the shopping_list using the pop method - removes item at given index.
print(shopping_list)
"""
Ran into confusion here, but below code doesn't work b/c I'm not trying to use pop on shopping_list but
rather the list within the list. So instead what I need to do it access inner list, then apply pop to it. 
shopping_list.pop([5][1])
print(shopping_list)
"""
shopping_list[5].pop(1)
print(shopping_list)

