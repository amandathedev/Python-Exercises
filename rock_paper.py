print("Rock, Paper, Scissors")

player1 = input("Play 1, make your move: ")
player2 = input("Play 2, make your move: ")

# Refactor
if player1 == player2:
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins!")
    elif player2 == "paper":
        print("Player 2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins!")
    elif player2 == "scissors":
        print ("Player 2 wins!")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1 wins!")
    elif player2 == "rock":
        print("Player 2 wins!")
else:
    print("Something went wrong!")



# Version 1:

# if player1 == "rock" and player2 == "scissors":
#     print("Player 1 wins!")
# elif player1 == "rock" and player2 == "paper":
#     print("Player 2 wins!")
# elif player1 == "paper" and player2 == "rock":
#     print("Player 1 wins!")
# elif player1 == "paper" and player2 == "scissors":
#     print("Player 2 wins!")
# elif player1 == "scissors" and player2 == "rock":
#     print("Player 2 wins!")
# elif player1 == "scissors" and player2 == "paper":
#     print("Player 1 wins!")
# elif player1 == player2:
#     print("It's a tie!")
# else:
#     print("Something went wrong.")