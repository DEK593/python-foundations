"""Week 0 - checkpoint test #1 (returns, rolling windows, volatility, Bollinger bands, NaN handling). Score: 19/30."""


import numpy as np  # noqa: E402, F401
import pandas as pd  # noqa: E402, F401

from dati import build_price_dataframe  # noqa: E402

ESERCIZI = {
    "E1 discesa massima": (["discesa_max"], "Mini-test W0: discesa massima dall'apertura open → low"),
    "E2 volume a 2 giorni": (["vol_var_2"], "Mini-test W0: variazione % del volume a 2 giorni"),
    "E3 log a 5 giorni": (["log_ret_5"], "Mini-test W0: rendimento logaritmico a 5 giorni"),
    "E4 range su close di ieri": (["range_pct"], "Mini-test W0: range high-low in % del close di ieri"),
    "E5 vol 10g annualizzata": (["vol_10_ann"], "Mini-test W0: volatilità mobile 10g annualizzata"),
    "E6 Bollinger 15g 2.5σ": (["boll_sup", "boll_inf"], "Mini-test W0: Bollinger 15g 2.5σ"),
    "E7 minimo mobile del low": (["min_low_5"], "Mini-test W0: minimo mobile 5g del low"),
    "E8 NaN della vol": (["nan_vol"], "Mini-test W0: contare i NaN di una colonna rolling"),
}

# 🎯 Quanto sei sicura di OGNI esercizio? 50, 70 o 90. Scrivilo PRIMA di correggere.
SICUREZZA = {
    "E1 discesa massima": 50,
    "E2 volume a 2 giorni": 70,
    "E3 log a 5 giorni": 90,
    "E4 range su close di ieri": 50,
    "E5 vol 10g annualizzata": 90,
    "E6 Bollinger 15g 2.5σ": 90,
    "E7 minimo mobile del low": 70,
    "E8 NaN della vol": 90,
}


def risolvi(df: pd.DataFrame):
    r = {}  # risposte che NON sono colonne

    # E1 (3 pt) - Di quanto e' SCESO il titolo, al massimo, durante la giornata
    #             rispetto all'apertura DELLO STESSO giorno (decimale, es. -0.012). Valore <= 0.
    df["discesa_max"] = df["low"] / df["open"] -1

    # E2 (3 pt) - Variazione % del VOLUME rispetto a 2 giorni di borsa prima (decimale).
    df["vol_var_2"] = df["volume"] / df["volume"].shift(2) -1

    # E3 (3 pt) - Rendimento LOGARITMICO a 5 giorni del close (np e' gia' importato).
    df["log_ret_5"] = np.log(df["close"] / df["close"].shift(5))

    # E4 (3 pt) - Escursione della giornata (massimo meno minimo di OGGI)
    #             espressa come frazione del close di IERI (decimale).
    df["range_pct"] = (df["high"] - df["low"]) / df["close"].shift(1)

    # E5 (4 pt) - Volatilita' mobile a 10 giorni dei rendimenti semplici giornalieri del close,
    #             ANNUALIZZATA (252 giorni di borsa). Tutto in una colonna.
    df["ret"] = df["close"].pct_change()
    df["vol_10_ann"] = df["ret"].rolling(10).std() * np.sqrt(252)
     # E6 (4 pt) - Bande di Bollinger sul close: media mobile 15 giorni, ampiezza 2.5 deviazioni standard.
    #             Due colonne: banda superiore e banda inferiore.
    std = df["close"].rolling(15).std()
    df["boll_sup"] = df["close"].rolling(15).mean() + 2.5 * std
    df["boll_inf"] = df["close"].rolling(15).mean() - 2.5 * std

    # E7 (3 pt) - Il prezzo PIU' BASSO toccato negli ultimi 5 giorni (oggi compreso), dalla colonna low.
    df["min_low_5"] = df["low"].rolling(5).min()

    # E8 (3 pt) - Quanti NaN ha la colonna vol_10_ann? Con il codice, non a mano (un numero intero).
    r["nan_vol"] = df["vol_10_ann"].isna().sum()

    return df, r


def main() -> None:
    df, r = risolvi(build_price_dataframe(seed=27))
    pd.set_option("display.width", 200)
    print(df.tail(3).to_string())
    print()
    for k, v in r.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
