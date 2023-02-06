import pandas as pd
import numpy as np

def heiken_ashi_candles(dataframe):
    heiken_ashi = pd.DataFrame()
    heiken_ashi['Open'] = (dataframe['Open'] + dataframe['Close']) / 2
    heiken_ashi['High'] = dataframe[['High', 'Open', 'Close']].max(axis=1)
    heiken_ashi['Low'] = dataframe[['Low', 'Open', 'Close']].min(axis=1)
    heiken_ashi['Close'] = (heiken_ashi['Open'] + heiken_ashi['High'] + heiken_ashi['Low'] + dataframe['Close']) / 4
    return heiken_ashi


def divide_dataframe(dataframe, parts):
    length = len(dataframe)
    parts = length // parts
    divided_dfs = [dataframe.iloc[i:i + parts] for i in range(0, length, parts)]
    return divided_dfs