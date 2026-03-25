import random

secret_number = random.randint(1, 10)

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

# guess = int(input("Enter your guess: "))
try:
    guess = int(input("Enter your guess: "))
except KeyboardInterrupt:
    print("\nGame interrupted!")
    exit()

if guess == secret_number:
    print("🔥 Correst! You Win!")
else:
    print("❌ Wrong!")
    print("The correct number was: ", secret_number)