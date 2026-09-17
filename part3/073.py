str1 = input("Please type in a word: ")
str2 = input("Please type in a character: ")

start = 0
result = str1.find(str2, start)


if result >= 0:
    start = result + len(str2)
    result = str1.find(str2, start)
    if result >= 0:
        print(f"The second occurrence of the substring is at index {result}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")
    
