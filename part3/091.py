num1 = [12, 45, 2, 89, 33, 5]
massimo = num1[0]

for i in num1:
    if massimo < i:
        massimo = i

print(massimo)