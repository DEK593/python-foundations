portfolio = {'AAPL': 12000, 'GOOGL': 4000, 'TSLA': 15000, 'AMZN': 8000}


large_positions = {t: v for t, v in portfolio.items() if v > 10000}

print(large_positions)
