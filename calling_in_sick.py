from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)


calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

if actually_sick and sick_days > 0:
    calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
else:
    calling_in_sick = False

if calling_in_sick == True:
    print("I'm calling in sick today.")
else:
    print("I have to go to work today.")