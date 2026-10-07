raw_transazioni = ["  spesa:spesa_giornaliera:15.50  ", "  investimento:AAPL:150.00  ", "  spesa:affitto:450.00  ", "  spesa:spesa_giornaliera:22.30  ", "  investimento:BTC:50.00  ", "  spesa:bollette:85.00  ", "  investimento:AAPL:100.00  "]

budget_iniziale = 1000.0


clean = [c.upper().strip() for c in raw_transazioni]

inv = [v for v in clean if "INVESTIMENTO" in v]



diz = {t.split(':')[1] : float(t.split(':')[2]) for t in inv}

    

spesa = { v for  v in clean if "SPESA" in v}

risultato = sum( float(t.split(':')[2]) for t in clean if "SPESA" in t) 

print(f"investimenti effetuati {diz}")
print(f"categorie spese {spesa}")
print(f"budget rimasto {budget_iniziale - risultato:.2f}$")