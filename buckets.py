from kucoin.client import Market
from numpy import double
from candle import Candle
from counter import *
import pandas as pd
import time

client = Market(url="https://api.kucoin.com")
klineCoin =("BTC-USDT")
klineTime =("1min")
color = 'Gray'
duration = '1'
candles = []

def createCandle():
    # Updates data every 30 seconds
    klines = client.get_kline(klineCoin, klineTime)
    df = pd.DataFrame(
        klines, columns=["start", "open", "close", "high", "low", "volume", "amount"]
    )
    # Allows condensation of data to Candle Object
    endRow = df.shape[0]
    openAH = df["open"][0]
    highAH = df["high"].max()
    lowAH = df["low"].min()
    closeAH = df["close"][endRow - 1]
    voluemAH = "{:.2f}".format(df["volume"].astype(float).sum())
    candle = Candle(duration, color, openAH, highAH, lowAH, closeAH, voluemAH)
    getCandles(candle)
    #print(df)
    return df

# Adds candle objects to dictionary
def getCandles(candle):
    candles.append(candle)
    if len(candles) > 41:
        del candles[0]
    #print(candles)
    updateCandles()

# Adds candles dictionary back into DataFrame
def updateCandles():
    df = pd.DataFrame([x.as_dict() for x in candles])  
    dfData = df["Close"]
    for i in range(len(dfData)):
        if i == 0:
            prevData = 0
            curData = float(dfData[i])
        else:
            prevData = float(df.iat[i - 1, 5])
            curData = float(dfData[i])
        if prevData < curData:
            df.loc[i, "Color"] = "Green"
        elif prevData > curData:
            df.loc[i, "Color"] = "Red"
        else:
            df.loc[i, "Color"] = df.loc[i-1,"Color"]
    return df

def getDf():
    return updateCandles()

def makeCandles():
    while True:
        createCandle()
        time.sleep(10)
        # converted_num = str(no)
        # if converted_num.endswith("0"):
        #     print("\nUpdated Dictionary\n")
            #print(getDf())
        print("\nUpdated Dictionary\n")
        print(getDf())


makeCandles()