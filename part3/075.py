import time

# timer 1
lil = 0
# timer 2
lal = 0
#timer 3
lul = 0
#timer 4
ltl = 0

chose = input("seleziona timer o sveglia: ").lower().strip()

if not chose:
    print("scegli uno dei due")
elif chose == "timer":

    
    timer = int(input("scegli tempo timer: "))
    print(f"set timer {timer} seconds")
    while lil < timer:
        meta = timer // 2
        
        time.sleep(1)
        lil += 1
        print(f"{lil} secondi passati")
        if lil == meta:
            print(f"meta del tempo ({meta}) passato")
    print("tempo scaduto")
    chose2 = input("riavviare si o no ?").lower().strip()
    if chose2 == "si":
        chose3 = input("mantenere stesso timer di prima si o no ?").lower().strip()
        if chose3 == "si":
            lil = 0
            while lil < timer:
                meta = timer // 2
        
                time.sleep(1)
                lil += 1
                print(f"{lil} secondi passati")
                if lil == meta:
                    print(f"meta del tempo ({meta}) passato")
            print("tempo scaduto")
        else:
            timer2 = int(input("scegli tempo timer: "))  
            print(f"set timer {timer2} seconds")
            while lal < timer2:
                sms = timer2 // 2
                time.sleep(1)
                lal += 1
                print(f"{lal} secondi sono passati ")
                if lal == sms:
                    print(f"meta del tempo ({sms}) passato")
            print("tempo terminato")
else:
    sveglia = int(input("seleziona la lunghezza della sveglia: "))
    
    while lul < sveglia:
        time.sleep(1)
        lul += 1
        
    print("sveglia terminata")
    uscita = input("scrivere esc per spegnerla: ").lower().strip()
    if uscita == "esc".lower().strip():
        print("sveglia spenta")
                
    else:
        print("posticipata di 3 minuti")
        time.sleep(180)
                
                
            





