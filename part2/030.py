# Fix the program
number = int(input("Please type in a number: "))

if number > 100:
    number -= 100
    print("The number was greater than one hundred")
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {number}")
    print(f"{number} must be my lucky number!")
    print("Have a nice day!")
elif number <= 100:
    print(f"{number} must be my lucky number!")
    print("Have a nice day!")