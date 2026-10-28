"""Synthetic OHLCV market data (reproducible with a seed), shared by all exercises."""

from __future__ import annotations

import numpy as np
import pandas as pd


def build_price_dataframe(n: int = 80, seed: int | None = 23, start: str = "2024-06-03") -> pd.DataFrame:
    """n giorni di borsa con open, high, low, close, volume. Stesso seed -> stessi dati."""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range(start, periods=n)
    close = rng.uniform(40, 250) * np.exp(np.cumsum(rng.normal(0.0002, 0.014, n)))
    open_ = close * (1 + rng.normal(0, 0.005, n))
    high = np.maximum.reduce([open_, close, close * (1 + np.abs(rng.normal(0, 0.007, n)))])
    low = np.minimum.reduce([open_, close, close * (1 - np.abs(rng.normal(0, 0.007, n)))])
    volume = rng.integers(400_000, 2_500_000, n).astype(float)
    return pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": volume},
        index=dates,
    )
