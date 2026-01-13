import random

# User defines the range
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

# Generate random number in the given range
secret_number = random.randint(low, high)
attempts = 0

print(f"\n🎯 Guess the number between {low} and {high}")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
        break
