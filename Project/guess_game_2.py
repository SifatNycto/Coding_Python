import random

secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 5

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print("🔥 Correst! You Win!")
        break
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Too low")
        
if attempts == max_attempts and guess != secret_number:
    print("Game Over!")
    print("The correct number was: ", secret_number)
