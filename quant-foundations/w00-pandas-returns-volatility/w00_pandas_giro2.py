"""Week 0, day 1 - simple and log returns with shift()."""

import numpy as np
import pandas as pd


def build_price_dataframe(n: int = 60, seed: int = 42) -> pd.DataFrame:
    """Dati OHLCV finti ma coerenti (low <= open, close <= high)."""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range("2024-01-02", periods=n)
    close = 100 * np.exp(np.cumsum(rng.normal(0.0005, 0.01, n)))
    open_ = close * (1 + rng.normal(0, 0.003, n))
    high = np.maximum.reduce([open_, close, close * (1 + np.abs(rng.normal(0, 0.005, n)))])
    low = np.minimum.reduce([open_, close, close * (1 - np.abs(rng.normal(0, 0.005, n)))])
    volume = rng.integers(500_000, 3_000_000, n).astype(float)
    return pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": volume},
        index=dates,
    )


def main() -> None:
    df = build_price_dataframe()

    # ------------------------------------------------------------------
    # ES 1 (EP 1.1) - Rendimento semplice: prezzo di oggi / prezzo di ieri - 1
    

    # ES 2 (EP 1.2) - Rendimento logaritmico: ln(oggi / ieri), usando shift
  

    # ES 3 (EC 2.5) - Variazione in euro rispetto a ieri


    # ES 4 (EC 2.6) - Range giornaliero: massimo - minimo della giornata


    # ES 5 (EC 3.5) - Gap di apertura: apertura di oggi vs chiusura di ieri
    
    # ------------------------------------------------------------------

    print(df[["close", "ret", "log_ret", "diff", "range", "gap"]].head(4).round(4).to_string())

    # --- Controlli automatici (non modificarli) ---
    c, o = df["close"], df["open"]
    assert np.allclose(df["ret"].iloc[1:], (c / c.shift(1) - 1).iloc[1:]), "ES 1 sbagliato"
    assert np.allclose(df["log_ret"].iloc[1:], np.log(c / c.shift(1)).iloc[1:]), "ES 2 sbagliato"
    assert np.allclose(df["diff"].iloc[1:], (c - c.shift(1)).iloc[1:]), "ES 3 sbagliato"
    assert np.allclose(df["range"], df["high"] - df["low"]), "ES 4 sbagliato"
    assert np.allclose(df["gap"].iloc[1:], (o / c.shift(1) - 1).iloc[1:]), "ES 5 sbagliato"
    assert df["ret"].isna().iloc[0], "La prima riga di ret dovrebbe essere NaN: perche'?"
    print("\nTutti e 5 giusti!")


if __name__ == "__main__":
    main()
