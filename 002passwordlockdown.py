import time


ADMIN_USERS = {"admin", "root"}

violazioni = 0
MAX_VIOLAZIONI = 3
tempo_blocco = 5  

print("--- SISTEMA DI LOGIN SICURO (BLINDATO) ---")

while True:
    try:
        
        tentativo = input("Inserisci username: ").strip().lower()

       
        if not tentativo.isalnum():
            print(" L'input non può essere vuoto.")
            continue

      
        if tentativo in ADMIN_USERS:
            print(" Accesso negato: Utente protetto o non autorizzato.")
            violazioni += 1
            print("Tentativo", violazioni)

           
            if violazioni >= MAX_VIOLAZIONI:
                print(" LOCKDOWN ATTIVATO. Sistema bloccato.")
                
              
                time.sleep(tempo_blocco)
                
                print("[*] Sblocco automatico completato.")
              
                tempo_blocco *= 2
             
                violazioni = 0
            continue

       
        print("Login effettuato con successo per l'utente")
        break

    except KeyboardInterrupt:
        print("Uscita forzata dal sistema.")
        break