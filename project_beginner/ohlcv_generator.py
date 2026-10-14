import numpy as np
import pandas as pd

def build_price_dataframe() -> pd.DataFrame:
    """Return a synthetic OHLCV DataFrame indexed by business date."""
    np.random.seed(42)
    dates = pd.bdate_range("2024-01-02", periods=60)
    close = 100 * np.cumprod(1 + np.random.normal(0.0005, 0.012, 60))
    high = close * (1 + np.abs(np.random.normal(0, 0.006, 60)))
    low = close * (1 - np.abs(np.random.normal(0, 0.006, 60)))
    open_ = close * (1 + np.random.normal(0, 0.005, 60))
    volume = np.random.randint(500_000, 5_000_000, 60).astype(float)

    df = pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": volume},
        index=dates,
    )
    df.index.name = "date"
    return df

if __name__ == "__main__":
    df = build_price_dataframe()
    print(df.head())