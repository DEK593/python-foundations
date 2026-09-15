str1 = input("Please type in a string: ")
hash = "*"
long = len(str1)

if long < 20:
    n1 = 20 - long
    print(n1 * hash+str1)
else:
    print(str1)