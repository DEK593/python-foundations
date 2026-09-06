temp = int(input("Please type in a temperature (F): "))

celsius = (temp - 32) / 1.8

print(f"{temp} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print("Brr! It's cold in here!")