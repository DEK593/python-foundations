chet = ""
last = ""

while True:
    name = input("Please type in a word: ")
    
    if name == "end":
        break
    if name == last:
        break

    chet += name + " "
    last = name 
print(chet)