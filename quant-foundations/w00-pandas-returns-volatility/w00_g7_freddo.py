"""Week 0, day 7 - closed-book drill: volume change, high-low range, rolling min, sample std by hand."""


import numpy as np  # noqa: E402, F401
import pandas as pd  # noqa: E402, F401

from dati import build_price_dataframe  # noqa: E402

# exercise -> (checked columns, review item)
ESERCIZI = {
    "Q1 volume a 2 giorni": (["vol_var_2"], "Mini-test W0: variazione % del volume a 2 giorni"),
    "Q2 range su close di ieri": (["range_pct"], "Mini-test W0: range high-low in % del close di ieri"),
    "Q3 minimo mobile del low": (["min_low_5"], "Mini-test W0: minimo mobile 5g del low"),
    "Q4 std passo per passo": (["std_manuale"], "Deviazione standard passo per passo (media → scarti → quadrati → n-1 → radice)"),
}

# 🎯 Quanto sei sicura di OGNI esercizio? 50, 70 o 90. Scrivilo PRIMA di correggere.
SICUREZZA = {
    "Q1 volume a 2 giorni": None,
    "Q2 range su close di ieri": None,
    "Q3 minimo mobile del low": None,
    "Q4 std passo per passo": None,
}


def risolvi(df: pd.DataFrame):
    r = {}  # risposte che NON sono colonne

    # Q1 - Variazione % del VOLUME rispetto a 2 giorni di borsa prima (decimale, es. 0.15).
    df["vol_var_2"] = df["volume"] / df["volume"].shift(2) -1

    # Q2 - Escursione della giornata (massimo meno minimo di OGGI)
    #      espressa come frazione del close di IERI (decimale).
    df["range_pct"] = (df["high"] - df["low"]) / df["close"].shift(1)

    # Q3 - Il prezzo PIU' BASSO toccato negli ultimi 5 giorni (oggi compreso), dalla colonna low.
    df["min_low_5"] = df["low"].rolling(5).min()

    # Q4 - Deviazione standard (campionaria) dei rendimenti semplici giornalieri del close,
    #      calcolata PASSO PER PASSO: VIETATO usare .std() o np.std().
    #      Una variabile per ogni passo (ti servira' anche .dropna()), alla fine un numero.
    ret = (df["close"] / df["close"].shift(1) -1).dropna()
    media = ret.mean()
    scarti = ret - media
    quadrati = scarti **2
    varianza = quadrati.sum() / (len(ret) -1)
    r["std_manuale"] = np.sqrt(varianza)

    return df, r


def main() -> None:
    df, r = risolvi(build_price_dataframe(seed=28))
    pd.set_option("display.width", 200)
    print(df.tail(3).to_string())
    print()
    for k, v in r.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
