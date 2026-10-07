def main():

    raw_tickers = ['aapl', ' MSFT ', 'GOOGL', 'aapl', 'tsla', '  AMZN  ', 'msft', 'NFLX', 'nvda', 'aapl ']


    portfolio_values = {'AAPL': 15000, 'MSFT': 8000, 'GOOGL': 25000, 'NVDA': 12000}


    prices = [145.5, 148.2, 146.0, 152.4, 151.0, 155.8]

    clear = {s.upper().strip() for s in raw_tickers}

    port_sum =sum(portfolio_values.values())

    analysis = {ticker: value / port_sum for ticker, value in portfolio_values.items()}

    price_dynamics = [(pr2 - pr1 ) / pr1 for pr1, pr2 in  zip(prices[:-1], prices[1:])]  # noqa: RUF007

    change = [r * 100 for r in price_dynamics ]
    
    print(f"raw_tickers cleared: {clear}")
    print(f"percentage weight: {analysis}")
    print("Price Change:")

    for c in change:
        print(f"{c:.2f}%")

if __name__== "__main__":
    main()