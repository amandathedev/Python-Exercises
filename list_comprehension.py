my_list = ["Elie", "Tim", "Matt"]

answer = [name[0] for name in my_list]
print(answer)

# Second exercise
list_two = [1,2,3,4,5,6]

answer2 = [num for num in list_two if num % 2 == 0]
print(answer2)

# Third exercise
list_three = [1,2,3,4]
list_four = [3,4,5,6]

answer3 = [num for num in [1,2,3,4] if num in [3,4,5,6]]
print(answer3)

# Fourth exercise
list_five = ["Elie", "Tim", "Matt"]

answer4 = [name[::-1].lower() for name in list_five]
print(answer4)