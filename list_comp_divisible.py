# https://www.udemy.com/the-modern-python3-bootcamp/learn/v4/t/quiz/406520

# Using a loop
for i in range(1,101):
    if i % 12 == 0:
        print(i)

# Using a list comprehension
answer = [val for val in range(1,101) if val % 12 == 0]