raw_tickers = [
    'aapl', ' MSFT ', 'GOOGL', 'aapl', 'tsla', 
    '  AMZN  ', 'msft', 'NFLX', 'nvda', 'aapl ', 
    'META', '  tsla', 'GOOGL', 'nflx', '  nvda  '
]


unique_symbols = {t.upper().strip() for t in raw_tickers}

print(unique_symbols)
