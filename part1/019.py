
mean = 0
sum = 0
times = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical lunch?"))
mean_price = float(input("How much money do you spend on groceries in a week?"))

sum = (price * times) + mean_price
mean = sum / 7

print("Average food expenditure")
print(f"Daily: {mean} euros")
print(f"Weekly: {sum} euros")