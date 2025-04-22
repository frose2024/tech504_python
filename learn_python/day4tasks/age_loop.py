user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) >= 117:
        print("Your age cannot be greater than 117")
        user_prompt = True
    elif age.isdigit() and int(age) <= 117:
        user_prompt = False
    else:
        print("Your age needs to be in the form of a positive integer")


