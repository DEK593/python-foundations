numeri = [1, 2, 3, 4, 5, 6, 7, 8]
elab = []

for i in numeri:
    if i % 2 == 0:
        prod = i * 10
        elab.append(prod)
print(elab)