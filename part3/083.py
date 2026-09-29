numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

risultati = []
for i in numeri:
    if i % 2 ==0:
        risultati.append(i * 2)
    else:
        risultati.append(i * 3)
print(risultati)