x = 1
while x <= 10:
    print("\U0001f603" * x)
    x += 1

# for loop version
for num in range(1,11):
    print("\U0001f606" * num)

# nested loop
for x in range(3):
    for num in range(1,11):
        print("\U0001f602" * num)