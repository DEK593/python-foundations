numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

risultati = []

for i in numeri:
    if i % 3 == 0:
        continue
    elif i % 2 == 0:
        risultati.append(i**2)
    else:
        risultati.append(i + 10)
print(risultati)