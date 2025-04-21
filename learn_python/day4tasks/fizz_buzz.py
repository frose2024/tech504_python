# Modulo is the best way to handle this

# Initialise fizz_counter to 1
fizz_counter = 1

fizz = input("What would like to fizz? ")
buzz = input("And what would you like to buzz? ")


while fizz_counter <= 100:

# If fizz_counter is divisible by both 5 and 3, print FizzBuzz
    if fizz_counter % 5 == 0 and fizz_counter % 3 == 0:
        print(f"{fizz}{buzz}")
        fizz_counter += 1


# If fizz_counter is divisible evenly by 3, print Buzz
    if fizz_counter % 3 == 0:
        print(f"{buzz}")
        fizz_counter += 1

# If fizz_counter is divisible evenly by 5, print Fizz
    if fizz_counter % 5 == 0:
        print(f"{fizz}")
        fizz_counter += 1

    else:
        print(fizz_counter)
        fizz_counter += 1