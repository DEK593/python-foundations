
def get_parameters():
    while True:
        try:
            price = float(input("minimun price: "))
            volume = int(input("minimun volume: "))
            return price, volume
        except ValueError:
            print("Error: You must enter a valid numeric value.")
def main():
    storico_borsa = [
        {"ticker": "AAPL", "close": 175.50, "volume": 50000, "signal": "BUY"},
        {"ticker": "TSLA", "close": 240.20, "volume": 12000, "signal": "HOLD"},
        {"ticker": "NVDA", "close": 480.00, "volume": 85000, "signal": "BUY"},
        {"ticker": "MSFT", "close": 320.10, "volume": 30000, "signal": "HOLD"},
        {"ticker": "AMD",  "close": 110.40, "volume": 60000, "signal": "BUY"},
        {"ticker": "AMZN", "close": 135.00, "volume": 45000, "signal": "SELL"}
]



    ticker = []           
        
    price, volume = get_parameters()       

    for i in storico_borsa:
        if i["close"] >= price and i["volume"] >= volume:
            ticker.append(i["ticker"])

    if len(ticker) == 0:
        print("None of the conditions are met")
    else:
        print(f"These are the stocks that meet your conditions: {', '.join(ticker)}")

if __name__== "__main__":
    main()