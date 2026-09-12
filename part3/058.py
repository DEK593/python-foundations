lista = {
"pane": 2.50,
"pasta":1.80,
"riso":3.40,
"farina":1.15,
"pollo": 10.00, 
"bovino": 16.50, 
"pesce": 9.50, 
"uova": 2.15,
}

cage = 0
#print(lista["pane"])
budget = int(input("inserire il budget massimo: "))

while cage <= budget:
    print("Digita q per uscire ")
    product = input("scegliere il prodotto desiderato: ").strip().lower()
    
    if product ==  "q".lower().strip():
        break
    if not product:
        print("prodotto non inserito")
        continue
    if product in lista:
        print(lista[product])
        price = lista[product]
    else:
        print("prodotto non disponibile")
        continue
    cage += price
    print(f"prezzo totale {cage}")
    if cage > budget:
        print(f"budget {budget} superato")
    
    

        
           

    
    
    

