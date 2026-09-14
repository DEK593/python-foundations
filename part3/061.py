string_1 = input("Please type in a string 1: ")
string_2 = input("Please tye in a string 2:")


str1 =len(string_1)
str2 =len(string_2)

if str1 > str2:
    print(f"{string_1} is longer")
        
elif str2 > str1:
    print(f"{string_2} is longer")
        
else:
    print("The strings are equally long")
        