sms = "-"

while True:
    str1 = input("Please type in a string: ")
    if not str1:
        break
    print(str1)
    print(len(str1) * sms)