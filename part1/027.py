wage = float(input("Hourly wage:"))
work = float(input("Hours worked:"))
day = input("Day of the week:")

if day != "Sunday":
    print(f"Daily wages: {wage * work} euros")
elif day == "Sunday":
    print(f"Daily wages: {wage * work * 2} euros")
