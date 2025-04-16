"""
x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

print(x + y + z)
"""
# Above code doesn't work b/c Python doesn't know how to add a string to a float
x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

print(str(x) + str(y) + z)
# Solution = casting x and y to strings using the str() method.