from math import sqrt

while True:
    num1 = int(input("Please type in a number: "))

    if num1 == 0 :
        break
    elif num1 < 0:
        print("Invalid number")
    else:
        print(sqrt(num1))
    


print("Exiting...")