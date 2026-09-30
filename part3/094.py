matrice = [
    [1, 2, 3],
    [4, 5, 6]
]

risultato = []


for i in range(3):
    

    nuova_riga = []
    
    
    for riga in matrice:

        nuova_riga.append(riga[i])
        
  
    risultato.append(nuova_riga)

print(risultato)