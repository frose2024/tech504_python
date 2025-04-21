import random

# Define/assign number to a variable called magic_number
magic_number = random.randrange(1,100)
guess_counter = 0
print(magic_number)

while guess_counter <= 4:
    guess = input("What's your guess? The magic number is between 1 and 100 - ")

    while guess.isdigit() == False:
        print("Sorry, you need to guess using a number. Try again ")
        guess = input("What's your guess? ")

    guess = int(guess)

    if guess == magic_number:
        guess_counter = 5
        print("Damn, you got it right.")
    elif guess > magic_number:
        guess_counter += 1
        print(f"Your guess was too high, try lower. You have used {guess_counter} guesses out of 5. ")
        if guess_counter >= 5:
            print(f"Sorry, you have run out of guesses. The correct answer was {magic_number}")
    elif guess < magic_number and guess_counter >= 5:
        guess_counter += 1
        print(f"Your guess was too low, try higher. You have used {guess_counter} guesses out of 5. ")
        if guess_counter >= 5:
            print(f"Sorry, you have run out of guesses. The correct answer was {magic_number}")


# Allow the user 5 guesses
