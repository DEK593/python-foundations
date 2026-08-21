import time

admin = "admin"
root = "root"
tempo_blocco = 5
violazioni = []
esc = "esc"

while True:
    password_inserita = input("insert user: ")
    
    if password_inserita == admin or password_inserita == root:
        print("accesso negato")
        violazioni.append(password_inserita)

        if len(violazioni) > 3:
            print("lockdown activated")
            
            while True:
                time.sleep(tempo_blocco)
                tentativo = input("insert user2: ")
                
                if tentativo == esc:
                    print("uscita consentita")
                    violazioni = []
                    tempo_blocco = 5
                    break
                elif tentativo == root or tentativo == admin:
                    print("accesso non consentito")
                    time.sleep(tempo_blocco)
                    tempo_blocco *=3
                else:
                    print("negato")
                    time.sleep(50)
                    

    if password_inserita == esc:
        print("Uscita eseguita.")
        break



















