import pandas as pd
import time
from kucoin.client import Market
client = Market(url="https://api.kucoin.com")
klines = client.get_kline("KCS-USDT", "1min")

no=-1
duration = 1
color = "TBD"
candles = []

class Candle:
    
    def __init__(self, no, duration, color, op3n, high, low, close, volume):
        self.no = no
        self.duration = duration
        self.color = color
        self.op3n = op3n
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __str__(self):
        return ("Candle " + str(self.no) + " " + str(self.duration) + "min " + str(self.color) + " " + str(self.op3n) + " " + str(self.high) + " " + str(self.low) + " " + str(self.close) + " " + str(self.volume))
   
    def __repr__ (self):
        return self.__str__()

    def createCandle(self, klines):
        df = pd.DataFrame(
            klines, columns=["start", "open", "close", "high", "low", "volume", "amount"]
        )
        endRow = df.shape[0]
        openAH = df["open"][0]
        highAH = df["high"].max()
        lowAH = df["low"].min()
        closeAH = df["close"][endRow - 1]
        voluemAH = "{:.2f}".format(df["volume"].astype(float).sum())
        candle = Candle(no, duration, color, openAH, highAH, lowAH, closeAH, voluemAH)
        self.getCandles(candle)

    def getCandles(self, candle):
        candles.append(candle)
        if len(candles) > 41:
            del candles[0]
        self.updateCandles()

    def updateCandles(self):
        df = pd.DataFrame([x.as_dict() for x in candles])
        dfData = df["close"]

        for i in range(len(dfData)):
            if i == 0:
                prevData = 0
                curData = dfData[i]
            else:
                prevData = df.iat[i - 1, 6]
                curData = dfData[i]
            if prevData < curData:
                df.loc[i, "color"] = "Green"
            elif prevData > curData:
                df.loc[i, "color"] = "Red"
            else:
                df.loc[i, "color"] = "Grey"
        return df

    def makeCandles(self, no, klines):
        while True:
            no += 1
            self.createCandle(klines)
            time.sleep(60)
            converted_num = str(no)
            if converted_num.endswith("0"):
                print("\nUpdated Dictionary\n")
                print(self.getDf())

    def getDf(self):
        return self.updateCandles()


Candle.makeCandles(no, klines)