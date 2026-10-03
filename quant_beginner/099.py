
portfolio = {'AAPL': 4000, 'MSFT': 6000, 'NVDA': 10000}


total = sum(portfolio.values()) 

portfolio_pct = {ticker: value / total for ticker, value in portfolio.items()}

print(portfolio_pct)
