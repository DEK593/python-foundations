catalogo = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Mouse", "price": 25, "stock": 0},
    {"name": "Tastiera", "price": 75, "stock": 12},
    {"name": "Monitor", "price": 300, "stock": 3},
    {"name": "Cuffie", "price": 50, "stock": 20},
    {"name": "Webcam", "price": 45, "stock": 8}
]

num1 = int(input("choose the maximun price of the object: "))
num2 = int(input("choose the minimun number of stock: "))
name = []
for i in catalogo:
    if i["price"] <= num1 and i["stock"] >= num2:
        name.append(i["name"].upper())

if len(name) == 0:
    print("none of these products comply with your requests.")
else:
    print(f"object with price maximun {num1}$ and with stock minimun {num2}: {*name,}")