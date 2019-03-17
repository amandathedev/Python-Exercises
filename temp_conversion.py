fahrenheit = input("What is the temperature in Fahrenheit today? ")

celsius = (int(fahrenheit) - 32) / 1.8
celsius = round(celsius)

if celsius <= 0:
    print("That's " + str(celsius) + " degrees Celsius! It's freezing outside! Wear your coat.")
elif celsius > 0 and celsius <= 10:
    print("That's " + str(celsius) + " degrees Celsius! It's pretty chilly. Bring a jacket.")
elif celsius > 10 and celsius <= 25:
    print("That's " + str(celsius) + " degrees Celsius! It's fairly warm outside.")
else:
    print("That's " + str(celsius) + " degrees Celsius! It's hot outside!")

