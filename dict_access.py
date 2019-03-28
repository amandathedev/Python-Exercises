from random import choice
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

print(f"Your choice was {food}.")
quantity = bakery_stock.get(food)

if quantity:
    print(f"We have that. There are {quantity} left.")
else:
    print("We don't make that.")