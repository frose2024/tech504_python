# Guess the word with 4 hints to help.
# Here we're using the syntax x:y, wherein x is the starting index and y is the ending index.

original_word = "recommendation"
scramble_word = "eoommandretnic"

hint1_slice = original_word[4:6]
hint2_slice = original_word[-3:]
hint3_slice = original_word [7:10]
hint4_slice = original_word[:2]

print("Scrambled word: ", scramble_word)
print("Guess the original word from the scrambled version")
print("Here are some hints: ")

print("\nHint 1: The 5th and 6th letters are '" + hint1_slice + "'.")
print("Hint 2: The last 3 letters are '" + hint2_slice + "'.")
print("Hint 3: The 8th to 10th letters are '" + hint3_slice + "'.")
print("Hint 3: The first 2 letters are '" + hint4_slice + "'.")

print("\nWhat's your guess?")