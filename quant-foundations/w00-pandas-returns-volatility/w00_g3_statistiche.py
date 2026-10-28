"""Week 0 - summary statistics (mean vs median, scalar vs column) and annualisation."""

import numpy as np
import pandas as pd


def build_price_dataframe(n: int = 120, seed: int = 2026) -> pd.DataFrame:
    """Un titolo nuovo: 120 giorni di borsa, OHLCV coerenti."""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range("2024-05-01", periods=n)
    close = 80 * np.exp(np.cumsum(rng.normal(0.0006, 0.012, n)))
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

    # GIA' PRONTO: rendimento semplice giornaliero
    ret = df["close"].pct_change()

    # ==================================================================
    # EC 1.2 - Il rendimento MEDIO giornaliero
    rend_medio = df["ret"].pct_change().mean()


    # EC 1.3 - Il prezzo di chiusura "al centro", senza farti influenzare dagli estremi
    prezzo_centro = df["close"].median()

    # EC 2.1 - Il prezzo medio di chiusura
    prezzo_medio = df["close"].mean()

    # EC 2.2 - La volatilita' giornaliera dei rendimenti (su tutto il periodo)
    vol_giorno = df["vol"].std()

    # EC 2.3 - La volatilita' ANNUALIZZATA (su tutto il periodo)
    vol_anno = df["vol"] * 252

    # EC 2.4 - Il rendimento medio ANNUALIZZATO (approssimato)
    rend_anno = df["ret"] * 252

    # EC 3.3 - Lo Sharpe ratio annualizzato (su tutto il periodo, tasso privo di rischio = 0)
    sharpe = df["ret"] / df["non lo so"]

    # EC 2.7 - Il range giornaliero (massimo - minimo) MEDIO della serie
    range_medio = df["high"] - df["low"]

    # EC 2.8 - Il rendimento giornaliero PEGGIORE e la DATA in cui e' successo
    peggiore = df["close"].min()
    data_peggiore = df["close"].idxmin()
    # ==================================================================

    risposte = {
        "EC 1.2 rend_medio": rend_medio,
        "EC 1.3 prezzo_centro": prezzo_centro,
        "EC 2.1 prezzo_medio": prezzo_medio,
        "EC 2.2 vol_giorno": vol_giorno,
        "EC 2.3 vol_anno": vol_anno,
        "EC 2.4 rend_anno": rend_anno,
        "EC 3.3 sharpe": sharpe,
        "EC 2.7 range_medio": range_medio,
        "EC 2.8 peggiore": peggiore,
        "EC 2.8 data_peggiore": data_peggiore,
    }
    print("Le tue risposte:")
    for nome, valore in risposte.items():
        if isinstance(valore, (pd.Series, pd.DataFrame)):
            print(f"  {nome:<22} -> una COLONNA di {len(valore)} valori, non un numero!")
        else:
            print(f"  {nome:<22} -> {valore}")

    # --- Controlli automatici (non modificarli) ---
    attesi = {
        "EC 1.2 rend_medio": 0.0013541,
        "EC 1.3 prezzo_centro": 89.807264,
        "EC 2.1 prezzo_medio": 88.280291,
        "EC 2.2 vol_giorno": 0.0123160,
        "EC 2.3 vol_anno": 0.195514,
        "EC 2.4 rend_anno": 0.341219,
        "EC 3.3 sharpe": 1.745243,
        "EC 2.7 range_medio": 0.953317,
        "EC 2.8 peggiore": -0.026499,
        "EC 2.8 data_peggiore": pd.Timestamp("2024-10-03"),
    }
    giusti = 0
    print()
    for nome, atteso in attesi.items():
        tuo = risposte[nome]
        if tuo is None:
            print(f"  [ ]  {nome:<22} da fare")
            continue
        try:
            if isinstance(atteso, pd.Timestamp):
                ok = pd.Timestamp(tuo) == atteso
            else:
                ok = not isinstance(tuo, (pd.Series, pd.DataFrame)) and abs(float(tuo) - atteso) < 1e-5
        except (TypeError, ValueError):
            ok = False
        print(f"  [{'x' if ok else '!'}]  {nome:<22} {'giusto' if ok else 'SBAGLIATO'}")
        giusti += bool(ok)
    print(f"\n{giusti}/{len(attesi)} giusti  (obiettivo: almeno {int(np.ceil(0.6 * len(attesi)))})")


if __name__ == "__main__":
    main()
