from candleBase import getCandles
import pandas as pd

def getCandlesInterval():
    interval = input("Set candle interval: ")   
    interval = int(interval)
    data = getCandles()
    df = pd.DataFrame(data)
    for i in range(0, len(df), interval):
        print(df[i:i+interval].max())
    print(df)
    return df


while True:
    getCandles()
    getCandlesInterval()