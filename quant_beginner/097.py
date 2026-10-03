
prices = [10, 20, 30, 40, 50, 60, 70]
returns = [(p2 - p1) / p1 for p1, p2 in zip(prices[:-1], prices[1:])]  # noqa: RUF007


for f in returns:
    perc = f * 100
    print(f"{perc:.2f}%")

