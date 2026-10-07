from math import log


raw_tickers = ["  aapl ", "msft", "aapl", "GOOGL", "  msft  ", "TSLA", "googl"]


raw_prices = ["150.50", "310.25", "2850.80", "125.40"]


portfolio_values = {"AAPL": 12000, "MSFT": 8500, "GOOGL": 35000, "TSLA": 4000}


price_history = [100, 103, 101, 107, 110, 108]

clean = {t.upper().strip() for t in raw_tickers}
clean_prices = list(map(float, raw_prices))

filters = {t: v for t, v in portfolio_values.items() if v > 10000 }

prices = [(ps2 - ps1) / ps1 for ps1, ps2 in zip(price_history[:-1], price_history[1:])]  # noqa: RUF007
generator = (log(price_history[i+1]/ price_history[i]) for i in range(len(price_history)-1))



print(clean)
print(clean_prices)
print(filters)

for n in generator:
    print(n)

for s in prices:
    rir = s * 100
    print(f"{rir:.2f}%")



