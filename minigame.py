import random

secret = random.randint(1, 50)
tries = 0
while True:
    numero_inserito = int(input("enter a number (1 to 50):"))
    if numero_inserito < secret:
        print("too low")
        tries += 1
    elif numero_inserito > secret:
        tries += 1
        print("too high")
    else:
        print("correct")
        break
    if tries >= 5:
        print("you lost")
        break   
