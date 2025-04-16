# Starting code
mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)

# Print the 2nd and 3rd items in the list.
print(mixture[1:3])

# Print every second item in the list - uses the syntax list[start index:stopping index:step], where step is how many items to skip
# [::2] translates to - start at the beginning (left blank), end at the end (left blank), step = 2
print(mixture[::2])

# Start at the last item, stop at the 3rd item, printing them out in reverse.
# Same principle as above, but using '-' reverses the step so it prints in reverse.
print(mixture[5:3:-1])