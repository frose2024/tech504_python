import random

# Define/assign number to a variable called magic_number
magic_number = random.randrange(1,100)
guess_counter = 1
print(magic_number)

while guess_counter <= 5:
    guess = input("What's your guess? The magic number is between 1 and 100 - ")

    while not guess.isdigit():
        print("Sorry, you need to guess using a number. Try again ")
        guess = input("What's your guess? The magic number is between 1 and 100 - ")

    guess = int(guess)

    if guess == magic_number:
        print("Damn, you got it right.")
        break
    elif guess > magic_number:
        print(f"Your guess was too high, try lower. You have used {guess_counter} guesses out of 5. ")
    else:
        print(f"Your guess was too low, try higher. You have used {guess_counter} guesses out of 5. ")

    guess_counter += 1

    if guess_counter > 5:
        print(f"Sorry, you have run out of guesses. The correct answer was {magic_number}")



