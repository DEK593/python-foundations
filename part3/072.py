
str1 = input("Please type in a word: ")
str2 = input("Please type in a character: ")
start = 0

result = str1.find(str2, start)

while  result != -1:
    if result >= 0 and len(str1) - result >= 3:
        index = result + 3
        print(str1[result:index])
    start = result + 1
    result = str1.find(str2, start)
    
