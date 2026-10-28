"""Week 0, day 5 - spaced-repetition drill."""

from pathlib import Path

import numpy as np
import pandas as pd


def build_price_dataframe(n: int = 90, seed: int = 26) -> pd.DataFrame:
    """Un titolo NUOVO: 90 giorni di borsa, OHLCV coerenti."""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range("2024-09-02", periods=n)
    close = 85 * np.exp(np.cumsum(rng.normal(0.0003, 0.015, n)))
    open_ = close * (1 + rng.normal(0, 0.006, n))
    high = np.maximum.reduce([open_, close, close * (1 + np.abs(rng.normal(0, 0.008, n)))])
    low = np.minimum.reduce([open_, close, close * (1 - np.abs(rng.normal(0, 0.008, n)))])
    volume = rng.integers(300_000, 3_000_000, n).astype(float)
    df = pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": volume},
        index=dates,
    )
    # (servizio) rendimento semplice giornaliero del close, gia' pronto: usalo dove serve
    df["ret"] = df["close"].pct_change()
    return df


def main() -> None:
    df = build_price_dataframe()

    # ==================================================================
    # PARTE A - GLI SBAGLIATI (livello 0), dal piu' sbagliato
    # ==================================================================
    # A1 - Rendimento intraday: dall'apertura alla chiusura DELLO STESSO giorno (in %)
    df["intraday"] = df["close"] / df["open"] -1

    # A2 - Volatilita' mobile a 20 giorni del VOLUME
    #      (deve essere confrontabile tra un titolo grande e uno piccolo)
    df["vol_volume_20"] = df["volume"].pct_change().rolling(20).std()

    # A3 - Volatilita' mobile a 20 giorni dei rendimenti, espressa su base SETTIMANALE
    df["vol_20_sett"] = df["ret"].rolling(20).std() * np.sqrt(5)

    # A4 - Quanto e' salito il titolo, al massimo, durante la giornata
    #      rispetto all'apertura DELLO STESSO giorno (in %)
    df["open_to_high"] = df["high"] / df["open"] -1

    # A5 - Range giornaliero in euro: quanto si e' mosso il prezzo tra massimo e minimo del giorno
    df["range_eur"] = df["high"] - df["low"]

    # A6 - Una colonna che, nella riga di OGGI, contiene il close di DOMANI
    df["close_domani"] = df["close"].shift(-1)

    # A7 - Media mobile a 20 giorni del close e volatilita' mobile a 20 giorni (dei rendimenti)
    df["sma_20"] = df["close"].rolling(20).mean()
    df["vol_20"] = df["ret"].rolling(20).std()
    # A8 - Conta i NaN di ciascuna delle due colonne, CON IL CODICE (non a mano)
    nan_sma_20 = df["sma_20"].isna().sum()
    nan_vol_20 = df["vol_20"].isna().sum()

    # ==================================================================
    # PARTE B - LIVELLO 1 (giusti la volta scorsa: se oggi sono giusti, salgono a +7)
    # ==================================================================
    # B1 - Rendimento a 5 giorni del close (in %)
    df["ret_5"] = df["close"].pct_change(5)

    # B2 - Bande di Bollinger a 20 giorni, 2 sigma (banda superiore e inferiore)
    std = df["close"].rolling(20).std()
    df["bb_su"] = df["sma_20"] + 2 * std
    df["bb_giu"] = df["sma_20"] - 2 * std

    # B3 - Volatilita' mobile a 20 giorni ANNUALIZZATA (parti da vol_20 di A7)
    df["vol_20_ann"] = df["vol_20"] * np.sqrt(252)

    # B4 - Variazione giornaliera del close in EURO
    df["var_eur"] = df["close"].diff()

    # B5 - Gap di apertura in %   |   B6 - Gap di apertura in euro
    df["gap_pct"] = df["open"] / df["close"].shift(1) -1
    df["gap_eur"] = df["open"] - df["close"].shift(1) 

    # B7 - Medie mobili del close: veloce a 10 giorni e lenta a 30 giorni
    df["sma_10"] = df["close"].rolling(10).mean()
    df["sma_30"] = df["close"].rolling(30).mean()

    # B8 - Massimo mobile del close a 20 giorni
    df["max_20"] = df["close"].rolling(20).max()

    # B9 - Rendimento a 3 giorni calcolato sulle APERTURE (in %)
    df["ret_open_3"] = df["open"].pct_change(3)

    # B10 - Bande di Bollinger a 10 giorni, 1.5 sigma
    std_2 = df["close"].rolling(10).std()
    df["bb10_su"] = df["sma_10"] + 1.5 * std_2
    df["bb10_giu"] = df["sma_10"] - 1.5 * std_2
    # ==================================================================

    pd.set_option("display.width", 200)
    for gruppo in (["close", "intraday", "open_to_high", "range_eur", "close_domani"],
                   ["vol_volume_20", "vol_20_sett", "sma_20", "vol_20", "vol_20_ann"],
                   ["ret_5", "bb_su", "bb_giu", "var_eur", "gap_pct", "gap_eur"],
                   ["sma_10", "sma_30", "max_20", "ret_open_3", "bb10_su", "bb10_giu"]):
        print(df[gruppo].tail(3).to_string())
        print()
    print(f"NaN sma_20: {nan_sma_20}   NaN vol_20: {nan_vol_20}")

    # --- Controlli automatici (non modificarli) ---
    # Per ogni colonna: (somma, somma dei valori assoluti, quanti NaN)
    attesi = {
        "A1 intraday": [("intraday", -0.009461, 0.436725, 0)],
        "A2 vol_volume": [("vol_volume_20", 70.745261, 70.745261, 20)],
        "A3 vol_sett": [("vol_20_sett", 2.656950, 2.656950, 20)],
        "A4 open_to_high": [("open_to_high", 0.686296, 0.686296, 0)],
        "A5 range_eur": [("range_eur", 115.960123, 115.960123, 0)],
        "A6 close_domani": [("close_domani", 7923.566587, 7923.566587, 1)],
        "A7 sma/vol": [("sma_20", 6289.387375, 6289.387375, 19),
                       ("vol_20", 1.188224, 1.188224, 20)],
        "A8 conta NaN": [],
        "B1 ret_5": [("ret_5", 0.957442, 2.433268, 5)],
        "B2 bollinger20": [("bb_su", 6631.114052, 6631.114052, 19),
                           ("bb_giu", 5947.660698, 5947.660698, 19)],
        "B3 vol_ann": [("vol_20_ann", 18.862472, 18.862472, 20)],
        "B4 var_eur": [("var_eur", 14.165507, 102.894145, 1)],
        "B5 gap_pct": [("gap_pct", 0.180245, 1.212811, 1)],
        "B6 gap_eur": [("gap_eur", 15.135978, 106.546830, 1)],
        "B7 sma 10/30": [("sma_10", 7198.820840, 7198.820840, 9),
                         ("sma_30", 5390.138248, 5390.138248, 29)],
        "B8 max_20": [("max_20", 6579.373024, 6579.373024, 19)],
        "B9 ret_open_3": [("ret_open_3", 0.617125, 2.109552, 3)],
        "B10 bollinger10": [("bb10_su", 7418.524420, 7418.524420, 9),
                            ("bb10_giu", 6979.117260, 6979.117260, 9)],
    }
    primo_file = Path(__file__).with_name("w00_g5_ripasso_PRIMO_LANCIO.txt")
    primo: dict[str, str] = {}
    if primo_file.exists():
        for riga in primo_file.read_text(encoding="utf-8").splitlines():
            if "=" in riga:
                k, v = riga.split("=", 1)
                primo[k] = v
    righe = []
    giusti = 0
    for nome, controlli in attesi.items():
        if nome.startswith("A8"):
            if nan_sma_20 is None and nan_vol_20 is None:
                righe.append(f"  [ ]  {nome:<16} da fare")
                continue
            try:
                ok = int(nan_sma_20) == 19 and int(nan_vol_20) == 20
            except (TypeError, ValueError):
                ok = False
        else:
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
