from random import randint
player_wins = 0
computer_wins = 0
winning_score = 5

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player score: {player_wins} \nComputer score: {computer_wins}")
    player = input("Rock, paper, scissors: ").lower()
    if player == "quit".lower():
        break
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
            player_wins += 1
        else:
            print("You lose!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("You win!")
            player_wins += 1
        else:
            print ("You lose!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
            player_wins += 1
        else:
            print("You lose!")
            computer_wins += 1
    else:
        print("Please enter a valid move!")

print(f"Final score is {player_wins} for you and {computer_wins} for the computer.")

if player_wins > computer_wins:
    print("Congratulations, you won!")
elif player_wins == computer_wins:
    print("It's a tie.")
else:
    print("Oh no, the computer won!")