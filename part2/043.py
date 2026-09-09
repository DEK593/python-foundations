gift = int(input("Value of gift:"))

if gift < 5000:
    print("No tax!")
elif gift >= 5000 and gift < 25000:
    print(f"Amount of tax: {(100 + (gift - 5000) *0.08)}")
elif gift >= 25000 and gift < 55000:
    print(f"Amount of tax: {(1700 + (gift - 25000) *0.10)}")
elif gift >= 55000 and gift < 200000:
    print(f"Amount of tax: {(4700 + (gift - 55000) *0.12)}")
elif gift >= 200000 and gift < 1000000:
    print(f"Amount of tax: {(22100 + (gift - 200000) *0.15)}")
elif gift >= 1000000:
    print(f"Amount of tax: {(142100 + (gift - 1000000) *0.17)}")