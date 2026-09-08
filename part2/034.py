num1 = int(input("Please type in the first number:"))
num2 = int(input("Please type in the second number:"))

if num1 > num2:
    print(f"the greater number was: {num1}")
elif num2 > num1:
    print(f"the greater number was: {num2}")
else:
    print("The numbers are equal")