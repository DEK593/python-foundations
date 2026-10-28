"""Week 0, day 3 - spaced-repetition drill (returns, rolling, volatility)."""

import numpy as np
import pandas as pd


def build_price_dataframe(n: int = 80, seed: int = 7) -> pd.DataFrame:
    """Un titolo NUOVO: 80 giorni di borsa, OHLCV coerenti."""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range("2024-03-01", periods=n)
    close = 50 * np.exp(np.cumsum(rng.normal(0.0003, 0.015, n)))
    open_ = close * (1 + rng.normal(0, 0.004, n))
    high = np.maximum.reduce([open_, close, close * (1 + np.abs(rng.normal(0, 0.006, n)))])
    low = np.minimum.reduce([open_, close, close * (1 - np.abs(rng.normal(0, 0.006, n)))])
    volume = rng.integers(500_000, 3_000_000, n).astype(float)
    return pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": volume},
        index=dates,
    )


def main() -> None:
    df = build_price_dataframe()

    # GIA' PRONTI (non sono in scadenza oggi): usali dove ti servono
    df["ret"] = df["close"].pct_change()
    df["sma_20"] = df["close"].rolling(20).mean()

    # ==================================================================
    # PARTE A - RIFAI A FREDDO (sbagliati il 21)
    # ==================================================================
    # F1 - Rendimento a 5 giorni: chiusura di oggi vs chiusura di 5 giorni fa (in %)
    df["ret_5"] = df["close"].pct_change(5)

    # F2 - Rendimento intraday: dall'apertura alla chiusura DELLO STESSO giorno (in %)
    df["intraday"] = df["close"] / df["open"] -1 

    # F3 - Volatilita' mobile a 20 giorni
    df["vol_20"] = df["ret"].rolling(20).std()

    # F4 - Bande di Bollinger a 20 giorni, 2 deviazioni standard
    std = df["close"].rolling(20).std()
    df["bb_upper"] = df["sma_20"] + 2 * std
    df["bb_lower"] = df["sma_20"] - 2 * std

    # F5 - Volatilita' mobile a 20 giorni ANNUALIZZATA (usa F3)
    df["vol_20_anno"] = df["ret"].rolling(20).std() * np.sqrt(252)

    # ==================================================================
    # PARTE B - VARIANTI MAI VISTE (una per ciascun esercizio della parte A)
    # ==================================================================
    # V1 - Rendimento a 20 giorni calcolato sulle APERTURE:
    #      apertura di oggi vs apertura di 20 giorni fa (in %)
    df["ret_open_20"] = df["open"].pct_change(20)

    # V2 - Quanto e' salito il titolo, al massimo, durante la giornata rispetto
    #      all'apertura DELLO STESSO giorno (in %)
    df["open_to_high"] = df["high"] / df["open"] -1

    # V3 - "Volatilita'" mobile a 20 giorni del VOLUME:
    #      quanto oscillano le variazioni % del volume, giorno per giorno
    
    df["vol_volume_20"] = df["volume"].pct_change().rolling(20).std()

    # V4 - Bande di Bollinger piu' strette e veloci: 10 giorni, 1.5 deviazioni standard
    std_10 = df["close"].rolling(10).std()
    df["bb10_upper"] = df["close"].rolling(10).mean() + 1.5 * std_10
    df["bb10_lower"] = df["close"].rolling(10).mean() - 1.5 * std_10

    # V5 - Volatilita' mobile a 20 giorni SETTIMANALE (una settimana = 5 giorni di borsa)
    #      (usa F3)
    df["vol_20_sett"] = df["ret"].rolling(20).std() * np.sqrt(5)
    # ==================================================================

    cols = ["close", "ret_5", "intraday", "vol_20", "bb_upper", "bb_lower", "vol_20_anno"]
    print(df[cols].tail(3).to_string())
    print()
    cols = ["ret_open_20", "open_to_high", "vol_volume_20", "bb10_upper", "bb10_lower", "vol_20_sett"]
    print(df[cols].tail(3).to_string())

    # --- Controlli automatici (non modificarli) ---
    # Per ogni colonna: (somma, somma dei valori assoluti, quanti NaN)
    attesi = {
        "F1 ret_5": [("ret_5", -0.939965, 1.910892, 5)],
        "F2 intraday": [("intraday", 0.05275, 0.222132, 0)],
        "F3 vol_20": [("vol_20", 0.790679, 0.790679, 20)],
        "F4 bollinger": [("bb_upper", 2749.701674, 2749.701674, 19),
                         ("bb_lower", 2422.157988, 2422.157988, 19)],
        "F5 vol_anno": [("vol_20_anno", 12.551645, 12.551645, 20)],
        "V1 ret_open_20": [("ret_open_20", -3.119793, 4.651454, 20)],
        "V2 open_to_high": [("open_to_high", 0.45796, 0.45796, 0)],
        "V3 vol_volume": [("vol_volume_20", 52.886334, 52.886334, 20)],
        "V4 bollinger 10": [("bb10_upper", 3118.951647, 3118.951647, 9),
                            ("bb10_lower", 2952.076244, 2952.076244, 9)],
        "V5 vol_sett": [("vol_20_sett", 1.768013, 1.768013, 20)],
    }
    giusti = 0
    print()
    for nome, controlli in attesi.items():
        colonne = [df[col] for col, _, _, _ in controlli]
        if all(c.isna().all() for c in colonne):
            print(f"  [ ]  {nome:<16} da fare")
            continue
        ok = True
        for (col, somma, somma_abs, n_nan), serie in zip(controlli, colonne):
            try:
                serie = serie.astype(float)
                ok = (
                    ok
                    and abs(serie.sum() - somma) < 1e-4
                    and abs(serie.abs().sum() - somma_abs) < 1e-4
                    and int(serie.isna().sum()) == n_nan
                )
            except (TypeError, ValueError):
                ok = False
        print(f"  [{'x' if ok else '!'}]  {nome:<16} {'giusto' if ok else 'SBAGLIATO'}")
        giusti += ok
    print(f"\n{giusti}/{len(attesi)} giusti")


if __name__ == "__main__":
    main()
