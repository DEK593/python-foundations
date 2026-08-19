import time 
violazioni = []
admin = "admin"
root = "root"
esci = "esci"
while True:
    parola_inserita = input("inserisci una parola:")

    if parola_inserita == admin or parola_inserita == root:
        print("comando sospetto rilevato")
        violazioni.append(parola_inserita)

    if len(violazioni) == 3:
        print("blocco attivato")
        time.sleep(20)
        violazioni = []

    if parola_inserita == esci:
         print(len(violazioni))
         break
   
        
 
