"""Week 0, day 4 - spaced-repetition drill."""

from pathlib import Path

import numpy as np
import pandas as pd


def build_price_dataframe(n: int = 80, seed: int = 23) -> pd.DataFrame:
    """Un titolo NUOVO: 80 giorni di borsa, OHLCV coerenti."""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range("2024-06-03", periods=n)
    close = 120 * np.exp(np.cumsum(rng.normal(0.0002, 0.014, n)))
    open_ = close * (1 + rng.normal(0, 0.005, n))
    high = np.maximum.reduce([open_, close, close * (1 + np.abs(rng.normal(0, 0.007, n)))])
    low = np.minimum.reduce([open_, close, close * (1 - np.abs(rng.normal(0, 0.007, n)))])
    volume = rng.integers(400_000, 2_500_000, n).astype(float)
    return pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": volume},
        index=dates,
    )


def main() -> None:
    df = build_price_dataframe()

    # ==================================================================
    # PARTE A - LIVELLO 1 (giusti il 20: se oggi sono giusti, tornano il 30)
    # ==================================================================
    # R1 - Rendimento semplice giornaliero del close (in %)
    df["ret"] = df["close"].pct_change()

    # R2 - Rendimento LOGARITMICO giornaliero del close
    df["log_ret"] = np.log(df["close"] / df["close"].shift(1))  

    # R3 - Range giornaliero in euro: quanto si e' mosso il prezzo tra massimo e minimo del giorno
    df["range_eur"] = df["high"] - df["low"]

    # ==================================================================
    # PARTE B - LIVELLO 0 (sbagliati ieri: rifalli a freddo)
    # ==================================================================
    # R4 - Rendimento a 10 giorni: chiusura di oggi vs chiusura di 10 giorni fa (in %)
    df["ret_10"] = df["close"] / df["close"].shift(10) -1

    # R5 - Rendimento intraday: dall'apertura alla chiusura DELLO STESSO giorno (in %)
    df["intraday"] = df["close"] / df["open"] -1

    # R6 - Quanto e' salito il titolo, al massimo, durante la giornata
    #      rispetto all'apertura DELLO STESSO giorno (in %)
    df["open_to_high"] = df["high"] / df["open"] -1 

    # R7 - "Volatilita'" mobile a 20 giorni del VOLUME:
    #      quanto oscillano le variazioni % del volume, giorno per giorno
    df["vol_volume_20"] = df["volume"].pct_change().rolling(20).std()

    # R8 - Volatilita' mobile a 20 giorni SETTIMANALE (una settimana = 5 giorni di borsa)
    df["vol_20_sett"] = df["ret"].rolling(20).std() * np.sqrt(5) 

    # ==================================================================
    # PARTE C - LE DUE DOMANDE APERTE (codice + risposta a parole)
    # ==================================================================
    # D1 - Una colonna che, nella riga di OGGI, contiene il close di DOMANI
    df["close_domani"] = df["close"].shift(-1)
    #      Poi rispondi a parole: perche' usare questa colonna per decidere
    #      se comprare OGGI, in un backtest, e' barare?
    risposta_d1 = "ma apparte che non puoi vedere il close di domani perche esce nan quindi non so perche dovrei intendere barare"

    # D2 - Media mobile a 20 giorni del close e volatilita' mobile a 20 giorni (usa R1)
    df["sma_20"] = df["close"].rolling(20).mean()
    df["vol_20"] = df["ret"].rolling(20).std()
    #      Conta i NaN di ciascuna delle due colonne, CON IL CODICE (non a mano)
    nan_sma_20 = df["sma_20"].isna().sum()
    nan_vol_20 = df["vol_20"].isna().sum()
    #      Poi rispondi a parole: perche' i due numeri sono diversi?
    risposta_d2 = ""
    # ==================================================================

    print(df[["close", "ret", "log_ret", "range_eur", "ret_10"]].tail(3).to_string())
    print()
    print(df[["intraday", "open_to_high", "vol_volume_20", "vol_20_sett", "close_domani"]].tail(3).to_string())
    print()
    print(f"NaN sma_20: {nan_sma_20}   NaN vol_20: {nan_vol_20}")
    print(f"D1: {risposta_d1 or '(vuota)'}")
    print(f"D2: {risposta_d2 or '(vuota)'}")

    # --- Controlli automatici (non modificarli) ---
    # Per ogni colonna: (somma, somma dei valori assoluti, quanti NaN)
    attesi = {
        "R1 ret": [("ret", -0.143202, 0.961854, 1)],
        "R2 log_ret": [("log_ret", -0.153271, 0.963908, 1)],
        "R3 range_eur": [("range_eur", 117.654828, 117.654828, 0)],
        "R4 ret_10": [("ret_10", -0.957709, 2.636265, 10)],
        "R5 intraday": [("intraday", -0.023101, 0.309139, 0)],
        "R6 open_to_high": [("open_to_high", 0.475728, 0.475728, 0)],
        "R7 vol_volume": [("vol_volume_20", 47.337882, 47.337882, 20)],
        "R8 vol_sett": [("vol_20_sett", 2.094341, 2.094341, 20)],
        "D1 close_domani": [("close_domani", 9192.202803, 9192.202803, 1)],
        "D2 sma/vol": [("sma_20", 7144.524222, 7144.524222, 19),
                       ("vol_20", 0.936618, 0.936618, 20)],
    }
    # Primo tentativo di ogni esercizio: salvato una volta sola, e' quello che conta
    primo_file = Path(__file__).with_name("w00_g4_ripasso_PRIMO_LANCIO.txt")
    primo: dict[str, str] = {}
    if primo_file.exists():
        for riga in primo_file.read_text(encoding="utf-8").splitlines():
            if "=" in riga:
                k, v = riga.split("=", 1)
                primo[k] = v
    righe = []
    giusti = 0
    for nome, controlli in attesi.items():
        colonne = [df[col] for col, _, _, _ in controlli]
        if all(c.isna().all() for c in colonne):
            righe.append(f"  [ ]  {nome:<16} da fare")
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
        if nome.startswith("D2"):
            try:
                ok = ok and int(nan_sma_20) == 19 and int(nan_vol_20) == 20
            except (TypeError, ValueError):
                ok = False
        primo.setdefault(nome, "giusto" if ok else "SBAGLIATO")
        righe.append(f"  [{'x' if ok else '!'}]  {nome:<16} {'giusto' if ok else 'SBAGLIATO'}"
                     f"   | 1° tentativo: {primo[nome]}")
        giusti += ok
    primo_file.write_text("".join(f"{k}={v}\n" for k, v in primo.items()), encoding="utf-8")
    al_primo = sum(v == "giusto" for v in primo.values())
    print()
    print("\n".join(righe))
    print(f"\nAdesso: {giusti}/{len(attesi)} giusti   |   AL PRIMO TENTATIVO (conta questo): "
          f"{al_primo}/{len(primo)} di quelli fatti")


if __name__ == "__main__":
    main()
