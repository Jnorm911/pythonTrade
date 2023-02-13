import pandas as pd
import numpy as np

def heiken_ashi_candles(dataframe):
    heiken_ashi = pd.DataFrame()
    heiken_ashi['Open'] = (dataframe['Open'] + dataframe['Close']) / 2
    heiken_ashi['High'] = dataframe[['High', 'Open', 'Close']].max(axis=1)
    heiken_ashi['Low'] = dataframe[['Low', 'Open', 'Close']].min(axis=1)
    heiken_ashi['Close'] = (heiken_ashi['Open'] + heiken_ashi['High'] + heiken_ashi['Low'] + dataframe['Close']) / 4
    return heiken_ashi


def df2():
    df3 = pd.DataFrame()
    for i in range(0, len(df), 4):
        df4 = df.iloc[i:i+4]
        endRow = df4.shape[0]
        openFix = df4["open"].iloc[0]
        highFix = df4["high"].max()
        lowFix= df4["low"].min()
        closeFix = df4["close"].iloc[endRow - 1]
        df5 = pd.DataFrame({'open': [openFix], 'high': [highFix], 'low': [lowFix], 'close': [closeFix]})
        df3 = pd.concat([df3, df5], ignore_index=True) 
    print("\n 4 minute candle \n")
    print(df3)
    return df3