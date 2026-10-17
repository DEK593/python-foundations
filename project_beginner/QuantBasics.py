import numpy as np  # noqa: F401, I001
import pandas as pd

def quant_basic(df: pd.DataFrame) -> None:
    print("QUANT-FOUNDATIONS")

np.random.seed(65)
n = 160
date = pd.bdate_range("2023-01-02", periods=n)
close = 100 * np.exp(np.cumsum(np.random.normal(0.0005, 0.01, n)))

open = close * (1 + np.random.normal(0, 0.003, n))
high = close * (1 + np.abs(np.random.normal(0, 0.005, n)))
low = close * (1 - np.abs(np.random.normal(0, 0.005, n)))
volume = np.random.randint(1_000_000, 5_000_000, n).astype(float)

df = pd.DataFrame(
    {"open": open, "high": high, "low": low, "close": close, "volume": volume},
    index=date,
)
