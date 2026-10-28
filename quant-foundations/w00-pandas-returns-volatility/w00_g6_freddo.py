"""Week 0, day 6 - closed-book drill: intraday high, 5-day return, log return."""


import numpy as np  # noqa: E402, F401
import pandas as pd  # noqa: E402, F401

from dati import build_price_dataframe  # noqa: E402

# exercise -> (checked columns, review item)
ESERCIZI = {
    "Q1 salita massima": (["salita_max"], "Salita massima dall'apertura open → high"),
    "Q2 ret_5": (["ret_5"], "Rendimento a n giorni `ret_5`"),
    "Q3 log_ret": (["log_ret"], "Rendimento logaritmico"),
}

# 🎯 Quanto sei sicura di OGNI esercizio? 50, 70 o 90. Scrivilo PRIMA di correggere.
SICUREZZA = {
    "Q1 salita massima": None,
    "Q2 ret_5": None,
    "Q3 log_ret": None,
}


def risolvi(df: pd.DataFrame):
    r = {}  # (oggi non serve: solo colonne)

    # Q1 - Quanto e' salito il titolo, al massimo, durante la giornata
    #      rispetto all'apertura DELLO STESSO giorno (in %)
    #sicurezza 50%
    df["salita_max"] = df["high"] / df["open"] -1

    # Q2 - Rendimento semplice a 5 giorni del close (in %)
    #sicurezza 90%
    df["ret_5"] = df["close"].pct_change(5)

    # Q3 - Rendimento logaritmico giornaliero del close
    #sicurezza 90%
    df["log_ret"] = np.log(df["close"] / df["close"].shift(1))

    return df, r


def main() -> None:
    df, r = risolvi(build_price_dataframe(seed=27))
    print(df.tail(3).to_string())


if __name__ == "__main__":
    main()
