age = input("How old are you? ")
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter but you can't drink.")
    elif age >= 21:
        print("Welcome! Have a look at our beer menu.")
    else:
        print("You can't come in. You are too young.")
else:
    print("Please show me your ID.")