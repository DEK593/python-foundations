string = input("Please type in a string: ")

indx = 1
while indx <= len(string):
    print(string[-indx:])
    indx += 1