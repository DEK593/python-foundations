"""Week 0, day 2 - closed-book drill: returns and shift()."""

import numpy as np
import pandas as pd


def build_price_dataframe(n: int = 60, seed: int = 42) -> pd.DataFrame:
    """Gli stessi dati finti di ieri (OHLCV coerenti)."""
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
    # RIFAI A FREDDO (sbagliati ieri)
    # ES 3 - Variazione in euro rispetto a ieri
    df["diff"] = df["close"].diff()

    # ES 5 - Gap di apertura in %: apertura di oggi vs chiusura di ieri
    df["gap"] = df["open"] / df["close"].shift(1) -1

    # VARIANTI MAI VISTE
    # V1 - Rendimento a 5 giorni: prezzo di oggi vs prezzo di 5 giorni fa (in %)
    df["ret_5"] = df["close"] / df["close"].shift(5) -1

    # V2 - Rendimento intraday: dall'apertura alla chiusura DELLO STESSO giorno (in %)
    df["intraday"] = df["close"] / df["open"] -1

    # V3 - Gap in euro (non in %): apertura di oggi vs chiusura di ieri
    df["gap_eur"] = df["open"] - df["close"].shift(1)
    # ------------------------------------------------------------------

    print(df[["open", "close", "diff", "gap", "ret_5", "intraday", "gap_eur"]].head(7).to_string())

    # --- Controlli automatici (non modificarli) ---
    # Per ogni colonna: (somma, somma dei valori assoluti, quanti NaN)
    attesi = {
        "ES 3 diff": ("diff", 6.806627, 39.601485, 1),
        "ES 5 gap": ("gap", 0.038934, 0.394412, 1),
        "V1 ret_5": ("ret_5", 0.305144, 0.69178, 5),
        "V2 intraday": ("intraday", 0.03383, 0.115551, 0),
        "V3 gap_eur": ("gap_eur", 3.861535, 40.453211, 1),
    }
    giusti = 0
    print()
    for nome, (colonna, somma, somma_abs, n_nan) in attesi.items():
        tuo = df[colonna]
        if tuo.isna().all():
            print(f"  [ ]  {nome:<12} da fare")
            continue
        try:
            tuo = tuo.astype(float)
            ok = (
                abs(tuo.sum() - somma) < 1e-4
                and abs(tuo.abs().sum() - somma_abs) < 1e-4
                and int(tuo.isna().sum()) == n_nan
            )
        except (TypeError, ValueError):
            ok = False
        print(f"  [{'x' if ok else '!'}]  {nome:<12} {'giusto' if ok else 'SBAGLIATO'}")
        giusti += ok
    print(f"\n{giusti}/5 giusti")


if __name__ == "__main__":
    main()
