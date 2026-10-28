# python-foundations

A structured, from-scratch path in Python programming, aimed at quantitative finance and machine learning engineering. Every exercise in this repository was written by hand and committed as I went, so the history reflects the actual learning process, mistakes included.

Started: September 2026.

## Repository structure

| Folder | Content | Files |
|---|---|---:|
| `part1/` | Core syntax: input/output, variables, conditionals (MOOC.fi Python Programming) | 29 |
| `part2/` | Loops, strings, functions (MOOC.fi) | 22 |
| `part3/` | Lists, nested loops, string processing (MOOC.fi) | 43 |
| `project_beginner/` | First small projects: OHLCV data generator, data cleaning, basic quant metrics | 7 |
| `quant_beginner/` | First quantitative exercises with NumPy and pandas | 8 |
| `quant-foundations/` | Structured quantitative finance curriculum, organised in weekly stages (see below) | ongoing |

## quant-foundations

A week-by-week curriculum that moves from pandas fundamentals to backtesting and machine learning:

- **Stage 0**: pandas for market data: returns, rolling windows, volatility, Bollinger bands, look-ahead bias
- **Stages 1-4**: functions and type hints with `assert` tests, data structures and Big-O, NumPy vectorisation, modules and classes (a reusable `qt/` package)
- **Stages 5-8**: real market data with pandas, plotting with matplotlib, Monte Carlo simulation, a vectorised backtest (SMA crossover vs buy and hold)
- **Stages 9-12**: scikit-learn, features and data leakage, PyTorch basics, a final end-to-end project

A stage is considered complete only after a closed-book checkpoint test with a score of at least 28/30.

Details and current status: [`quant-foundations/README.md`](quant-foundations/README.md)

## Progress

![First-try accuracy](quant-foundations/progress/accuracy.png)

Exercises are reviewed with spaced repetition (intervals of 3, 7, 14 and 30 days). Only a correct answer on the first attempt, without hints, counts as correct; anything else comes back the next day. Raw data: [`quant-foundations/progress/attempts.csv`](quant-foundations/progress/attempts.csv).

## Tools

Python 3.13, pandas, NumPy, Git. Synthetic OHLCV data is generated with a fixed seed so every result is reproducible.
