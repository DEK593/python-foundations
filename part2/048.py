
attempts = 0

while True:
    pin = input("PIN: ")
    attempts = attempts + 1
    if pin == "4321":
        break
    elif pin != "4321":
        print("Wrong")

if attempts == 1:
    print("Correct! It only took you one single attempt!")
elif attempts > 1:
    print(f"Correct! It took you {attempts} attempts")
    

