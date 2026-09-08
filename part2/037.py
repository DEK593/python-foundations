age = input("What is your age?")

if not age.strip():
    print("That must be a mistake")
else:
    età = int(age)

    if età <0:
        print("That must be a mistake")
    elif età <5:
        print("I suspect you can't write quite yet...")
    else:
        print(f"Ok, you're {età} years old")
    
