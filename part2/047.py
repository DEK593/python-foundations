passw = input("Password: ").strip().lower()
while True:
    passw2 = input("Repeat password: ").strip().lower()

    if passw == passw2:
        break
    else:
        print("They do not match!")


print("User account created!")