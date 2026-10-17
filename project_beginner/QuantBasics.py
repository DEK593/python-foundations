#%%
import numpy as np  # noqa: F401, I001
import pandas as pd
pd.set_option("display.max_rows", None)      
pd.set_option("display.max_columns", None)   
#%%
def quant_basic() -> pd.DataFrame:
    print("QUANT-FOUNDATIONS")
    print("HOLCV")

    np.random.seed(65)
    n = 160
    date = pd.bdate_range("2023-01-02", periods=n)
    close = 100 * np.exp(np.cumsum(np.random.normal(0.0005, 0.01, n)))

    open = close * (1 + np.random.normal(0, 0.003, n))
    high = close * (1 + np.abs(np.random.normal(0, 0.005, n)))
    low = close * (1 - np.abs(np.random.normal(0, 0.005, n)))
    volume = np.random.randint(1_000_000, 5_000_000, n).astype(float)

    df = pd.DataFrame(
        {"open": open, "high": high, "low": low, "close": close, "volume": volume},
        index=date,
    )
    df.index.name = "date"
    return df
        
df = quant_basic()
#%%
def return_and_rolling(df: pd.DataFrame) -> pd.DataFrame:
    print("RETURN AND ROLLING")
    df = df.copy()
    df["ret"] = df["close"].pct_change()
    df["log_ret"] = np.log(df["close"] / df["close"].shift(1))
    df["sma_55"] = df["close"].rolling(55).mean()
    df["volatility_55_ret"] = df["ret"].rolling(55).std()
    std = df["close"].rolling(55).std()
    df["upper-bb"] = df["sma_55"] + 2 * std
    df["lower-bb"] = df["sma_55"] - 2 * std
    df["sharpe"] =(df["ret"].rolling(55).mean() / df["ret"].rolling(55).std()) * np.sqrt(252)
    return df

df = return_and_rolling(df)
df.round(4)  
# %%
df.info()
# %%
