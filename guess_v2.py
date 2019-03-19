import random

answer = random.randint(1,10)
guess = input("Guess a number between 1 and 10: ")

while answer > int(guess):
    print("Too low, try again!")
    print(f"The answer was {answer}!")
    break
while answer < int(guess):
    print("Too high, try again!")
    print(f"The answer was {answer}!")
    break