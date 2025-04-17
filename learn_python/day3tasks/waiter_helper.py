# Script should act like a waiter at a restaurant taking orders

# level 1
# Greet the user
user_name = input("Welcome to Applebees. Table name? ")
print(f"Good evening {user_name}, let me show you to your table")

# Print a list of starters
starters = ["Boneless Wings", "Mozzarella Sticks", "Crispy Cheese Bites", "Breadsticks With Alfredo Sauce"]
print(f"To start we have the {starters[0]}, {starters[1]}, {starters[2]} or the {starters[3]}. No, none of it is vegan.")

# Take an input for the user for their starter
user_starter = input("What can we get for you? ")

# Print a list of mains
mains = ["Grilled Chicken Ceaser Salad","Bourbon Street Chicken and Shrimp", "Prime Rib Dipper", "Whisky Bacon Burger"]
print(f"For your main course, can I interest you in the {mains[0]}, the {mains[1]}, the {mains[2]} or the {mains[3]}? No, none of that was even vegetarian actually.")

# Take an input for the user for their main course
user_main = input("What would you like for your main course? ")

# Print a list of desserts
desserts = ["Blue Ribbon Brownie", "Brownie Bite", "Triple Chocolate Meltdown"]
print(f"Your dessert options are the {desserts[0]}, the {desserts[1]} or the {desserts[2]}. These are all vegetarian. But not vegan. Vegans don't really come here honestly.")

# Take an input for the user for their dessert
user_dessert = input("So which would you like? ")

# Print all of the user's choices
customer_order_list = [user_starter, user_main, user_dessert]
print(customer_order_list)

# level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.
prices = {
    "Boneless Wings" : 9.99,
    "Mozzarella Sticks" : 8.49,
    "Crispy Cheese Bites" : 6.99,
    "Breadsticks With Alfredo Sauce" : 5.99,
    "Grilled Chicken Ceaser Salad" : 10.59,
    "Bourbon Street Chicken and Shrimp" : 14.49,
    "Prime Rib Dipper" : 12.99,
    "Whisky Bacon Burger" : 11.29,
    "Blue Ribbon Brownie" : 6.99,
    "Brownie Bite" : 1.79,
    "Triple Chocolate Meltdown" : 6.99
}

# Access start list, retrieve value for key. Access main list, do the same. Repeat for dessert. Total.
user_bill = prices[user_starter] + prices[user_main] + prices[user_dessert]
print(f"{user_name}, your final bill for this evening is ${user_bill}. At Applebees, we're all family. Except for the vegans.")

# level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.
# Improvement would be storing everything in the dictionary as lower case and turning all user input to lower case w/ lower()