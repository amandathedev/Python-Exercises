import random

answer = random.randint(1,10)

while True:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if guess < answer:
        print("Too low, try again!")
    elif guess > answer:
        print("Too high, try again!")
    else:
        print("Congratulations! You won!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            answer = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing!")
            break