sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# https://stackoverflow.com/questions/1801668/convert-a-python-list-with-strings-all-to-lowercase-or-uppercase
sounds = [x.upper() for x in sounds]
# https://stackoverflow.com/questions/12453580/concatenate-item-in-list-to-strings/12453584
sound_string = ''.join(sounds)

# print(sounds)
print(sound_string)


# Alternative solutions
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()

# 2
