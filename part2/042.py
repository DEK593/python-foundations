l1 = input("1st letter:")
l2 = input("2st letter:")
l3 = input("3st letter:")

if l2 < l1 < l3 or l3 < l1 < l2:
    print(f"The letter in the middle is {l1}")
elif l1 < l2 < l3 or l3 < l2 < l1:
    print(f"The letter in the middle is {l2}")
elif l2 < l3 < l1 or l1 < l3 < l2:
    print(f"The letter in the middle is {l3}")
