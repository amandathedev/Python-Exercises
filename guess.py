import random


num = random.randint(1, 10)
guess = None
while guess != num:
	guess = input("Guess a number between 1 and 10: ")
	guess = int(guess)
	if guess == num:
		print("Congratulations! You won!")
		break
	else:
		print("Nope, sorry. Try again!")