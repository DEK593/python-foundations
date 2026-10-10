import math

raw_tickers = ["  aapl", "msft  ", "AAPL", "tsla", "  baba ", "TSLA"]

raw_prices = {
    "AAPL": ["150.0", "152.5", "149.0", "153.2", "155.0"],
    "MSFT": ["300.0", "298.0", "302.5", "305.0", "310.0"],
    "TSLA": ["200.0", "195.0", "190.0", "185.0", "180.0"],
    "BABA": ["80.0", "81.5", "81.0", "82.5", "82.0"],
}
raw_signals = [
    {"ticker": "AAPL", "strength": 0.88},
    {"ticker": "MSFT", "strength": 0.45},
    {"ticker": "TSLA", "strength": 0.12},
    {"ticker": "BABA", "strength": 0.79},
]
clean = {v.upper().strip() for v in raw_tickers}

cleaned_prices = {
    ticker: list(map(float, raw_prices[ticker])) for ticker in clean
}

filtered_signal = [sign for sign in raw_signals if sign['strength'] > 0.50] 

get = {v["ticker"] for v in filtered_signal}

crf = {ticker: cleaned_prices[ticker] for ticker in get}

gen = (math.log(crf["AAPL"][i+1]/crf["AAPL"][i])for i in range(len(crf["AAPL"]) -1)) 
for s in gen:
    print(s)


