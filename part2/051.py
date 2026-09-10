count = 0
sum_n = 0
mean = 0
positive = 0
negative = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num1 = input("Number: ")
    num1 = int(num1)
    if num1 == 0 :
        break
    elif num1 < 0:
        negative += 1
    elif num1 > 0:
        positive += 1

    count += 1
    sum_n += int(num1)
mean += sum_n / count
    
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum_n}")
print(f"The mean of the numbers is {mean:.2f}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")

    