from kucoin.client import Market
from candleClass import Candle
import pandas as pd
import time

client = Market(url="https://api.kucoin.com")
klineCoin =("BTC-USDT")
klineTime =("1min")
duration = '1'
candles = []

def createCandle():
    try:
        # Updates data every 30 seconds
        klines = client.get_kline(klineCoin, klineTime)
        df = pd.DataFrame(
            klines, columns=["start", "open", "close", "high", "low", "volume", "amount"]
        )
        # Creates DataFrame as a class object
        endRow = df.shape[0]
        openAH = df["open"][0]
        highAH = df["high"].max()
        lowAH = df["low"].min()
        closeAH = df["close"][endRow - 1]
        voluemAH = "{:.2f}".format(df["volume"].astype(float).sum())
        color = None
        candle = Candle(duration, color, openAH, highAH, lowAH, closeAH, voluemAH)
        getCandles(candle)
        #return candle
    except:
        print("\nError getting candle\n")
        pass

# Adds candle object to dictionary
def getCandles(candle):
    candles.append(candle)
    if len(candles) > 60:
        del candles[0]
    return candles

def candleInterval(candles):
    for i in range(0, len(df), minutes):
    print(df[i:i+minutes].max())


def candleColor():
    df = pd.DataFrame([x.as_dict() for x in candles])  
    dfData = df["Close"]
    # Changes Candle Color
    for i in range(len(dfData)):
        if i == 0:
            prevData = 0
            curData = float(dfData[i])
        else:
            prevData = float(df.iat[i - 1, 5])
            curData = float(dfData[i])
        if prevData == 0:
            df.loc[i, "Color"] = "Gray"
        elif prevData < curData:
            df.loc[i, "Color"] = "Green"
        elif prevData > curData:
            df.loc[i, "Color"] = "Red"
        else:
            df.loc[i, "Color"] = df.loc[i-1,"Color"]
    return df
   

def makeCandles():
    while True:
        createCandle()
        #print(getDf())
        time.sleep(5)
        print("\nUpdated Dictionary\n")

makeCandles()