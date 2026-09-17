
str1 = input("Please type in a word: ")
str2 = input("Please type in a character: ")

result = str1.find(str2)
index = result + 3

if result >= 0 and len(str1) - result > 3:
    print(str1[result:index])

