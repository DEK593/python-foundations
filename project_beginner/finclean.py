from functools import reduce  # noqa: F401, I001
from itertools import accumulate  # noqa: F401
import math  # noqa: F401
import operator  # noqa: F401

raw_tickers = ["  aapl", "msft  ", "AAPL", "tsla", "  baba ", "TSLA"]


raw_prices = {
"AAPL": ["150.0", "152.5", "149.0", "153.2", "155.0"],
"MSFT": ["300.0", "298.0", "302.5", "305.0", "310.0"],
"TSLA": ["200.0", "195.0", "190.0", "185.0", "180.0"],
"BABA": ["80.0", "81.5", "81.0", "82.5", "82.0"],
}

# Forza del segnale algoritmico calcolato (da 0 a 1)
raw_signals = [
{"ticker": "AAPL", "strength": 0.88},
{"ticker": "MSFT", "strength": 0.45},
{"ticker": "TSLA", "strength": 0.12},
{"ticker": "BABA", "strength": 0.79},
]

clean_data = {t.upper().strip() for t in raw_tickers}

formats = {
    ticker: list(map(float, raw_prices[ticker])) for ticker in clean_data
}

signals = [v for v in raw_signals if v["strength"] > 0.50]

estract = [v["ticker"] for v in signals]

aapl = formats["AAPL"]
aapl_return = [(aapl[i + 1]- aapl[i]) / aapl[i] for i in range(len(aapl) - 1)] 

rent = reduce(lambda x, r: x* (1 + r), aapl_return, 1.0) -1

acc = list(accumulate([1.0] + aapl_return, operator.mul))

print(f"return daily: {[f'{r:.3f}' for r in aapl_return]}")
print(f"equity curve: {[f'{v:.3f}' for v in acc]}")
print(f"total compost: {rent:.3f} ")



