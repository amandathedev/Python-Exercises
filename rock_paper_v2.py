from random import randint

player = input("Rock, paper, scissors: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}.")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif player == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print ("You lose!")
elif player == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("You lose!")
else:
    print("Please enter a valid move!")