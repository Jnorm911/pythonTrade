from kucoin.client import Market
from candleClass import Candle
import threading as t
import pandas as pd
import copy
import time

client = Market(url="https://api.kucoin.com")
klineCoin =("BTC-USDT")
klineTime =("1min")
duration = '1'
candles = []

def createCandle():
    try:
        # Updates data every 30 seconds(roughly)
        klines = client.get_kline(klineCoin, klineTime)
        # Creates DataFrame as a class object
        df = pd.DataFrame(
            klines, columns=["start", "open", "close", "high", "low", "volume", "amount"]
        )
        endRow = df.shape[0]
        openAH = df["open"][0]
        highAH = df["high"].max()
        lowAH = df["low"].min()
        closeAH = df["close"][endRow - 1]
        voluemAH = "{:.2f}".format(df["volume"].astype(float).sum())
        color = None
        candle = Candle(duration, color, openAH, highAH, lowAH, closeAH, voluemAH)
    except:
        print("\nError getting candle, Making new candle\n")
        candle = Candle(duration, color, openAH, highAH, lowAH, closeAH, voluemAH)
        pass
        print("after pass")
    return candle

# Adds candle objects to a candles dictionary
def candleDict():
    candles.append(createCandle())
    if len(candles) > 60:
        del candles[0]
    #print(candles)
    return candles

def getCandles():
    candles1 = candleDict()
    candlesCopy = copy.copy(candles1)
    return candlesCopy


def startCandleBase():
    while True:
        candleDict()
        time.sleep(1)