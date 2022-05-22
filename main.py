import random

# Write your code here.
# Make sure to use `random.randint` to pick your random number.

while True:
    try:
        start = int(input("Enter the start of the range: "))
        break
    except ValueError as e:
        print("Please enter a valid number.")

while True:
    try:
        end = int(input("Enter the end of the range: "))
        if end < start:
            print("Please enter a valid number.")
            continue
        else:
            break
    except ValueError as e:
        print("Please enter a valid number.")

rand_number = random.randint(int(start), int(end))

attempts = 0

while True:
    try:
        guess = int(input("Guess a number: "))
        attempts += 1

        if int(guess) == rand_number:
            if attempts > 1:
                print(f"You guessed the number in {attempts} attempts")
            else:
                print(f"You guessed the number in {attempts} attempt")
            break
    except ValueError as e:
        print("Please enter a valid number.")




