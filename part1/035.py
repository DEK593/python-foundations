print("Person 1:")

name = input("Name:")

age = int(input("age:"))

print("Person 2:")

name2 = input("Name:")

age2 = int(input("age:"))

if age > age2:
    print(f"The elder is {name}")
elif age2 > age:
    print(f"The elder is {name2}")
else:
    print(f"{name} and {name2} are the same age")
