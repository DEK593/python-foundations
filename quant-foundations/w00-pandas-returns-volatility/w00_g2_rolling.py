"""Week 0, day 2 - rolling windows: moving averages and rolling volatility."""

import numpy as np
import pandas as pd


def build_price_dataframe(n: int = 60, seed: int = 42) -> pd.DataFrame:
    """Gli stessi dati finti di sempre (OHLCV coerenti)."""
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
    # R0 - Rendimento semplice giornaliero (ti serve per R2 e R6)
    df["ret"] = df["close"].pct_change()

    # R1 (EP 1.3) - Media mobile semplice a 20 giorni del prezzo di chiusura
    df["sma_20"] = df["close"].rolling(20).mean()

    # R2 (EP 1.4) - Volatilita' mobile a 20 giorni
    df["vol_20"] = df["ret"].rolling(20).std() 

    # R3 (EP 2.1) - Bande di Bollinger a 20 giorni, 2 deviazioni standard
    std = df["close"].rolling(20).std()
    df["upper_bb"] = df["sma_20"] + 2 * std
    df["lower_bb"] = df["sma_20"] - 2 * std
    # R4 (EC 4.1) - Medie mobili a 10 e a 30 giorni
    df["sma_10"] = df["close"].rolling(10).mean()
    df["sma_30"] = df["close"].rolling(30).mean()

    # R5 (EC 4.3, variante) - Prezzo di chiusura MASSIMO degli ultimi 20 giorni
    df["max_20"] = df["close"].rolling(20).max()

    # R6 (variante) - Volatilita' mobile a 20 giorni ANNUALIZZATA
    df["vol_20_anno"] = df["vol_20"] * np.sqrt(252)

    # R7 (EC 5.5, trova l'errore) - Questa riga e' sbagliata: correggila
    df["sma_5"] = df["close"].rolling(5).mean()
    # ------------------------------------------------------------------

    cols = ["close", "sma_20", "vol_20", "upper_bb", "lower_bb", "max_20", "vol_20_anno"]
    print(df[cols].tail(4).to_string())

    # --- Controlli automatici (non modificarli) ---
    # Per ogni colonna: (somma dei valori, quanti NaN)
    attesi = {
        "R0 ret": [("ret", 0.06748, 1)],
        "R1 sma_20": [("sma_20", 4198.907853, 19)],
        "R2 vol_20": [("vol_20", 0.29692, 20)],
        "R3 bollinger": [("upper_bb", 4311.756314, 19), ("lower_bb", 4086.059392, 19)],
        "R4 sma 10/30": [("sma_10", 5226.059008, 9), ("sma_30", 3174.587043, 29)],
        "R5 max_20": [("max_20", 4297.238892, 19)],
        "R6 vol_anno": [("vol_20_anno", 4.713451, 20)],
        "R7 sma_5": [("sma_5", 5739.744627, 4)],
    }
    giusti = 0
    print()
    for nome, controlli in attesi.items():
        colonne = [df[col] for col, _, _ in controlli]
        if all(c.isna().all() for c in colonne):
            print(f"  [ ]  {nome:<13} da fare")
            continue
        ok = True
        for (col, somma, n_nan), serie in zip(controlli, colonne):
            try:
                serie = serie.astype(float)
                ok = ok and abs(serie.sum() - somma) < 1e-4 and int(serie.isna().sum()) == n_nan
            except (TypeError, ValueError):
                ok = False
        print(f"  [{'x' if ok else '!'}]  {nome:<13} {'giusto' if ok else 'SBAGLIATO'}")
        giusti += ok
    print(f"\n{giusti}/{len(attesi)} giusti")


if __name__ == "__main__":
    main()
