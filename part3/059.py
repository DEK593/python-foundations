limit = int(input("Limit: "))
number = 1
sum_val = 1
calc = "1"

while sum_val < limit:
    number += 1
    calc += f" + {number}"
    sum_val += number

print(f"The consecutive sum: {calc} = {sum_val}")