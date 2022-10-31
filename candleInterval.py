from candleBase import getCandles
import pandas as pd

# def getCandlesInterval():
#     interval = input("Set candle interval: ")   
#     interval = int(interval)
#     data = getCandles()
#     df = pd.DataFrame(data)
#     for i in range(0, len(df), interval):
#         print(df[i:i+interval].max())
#     print(df)
#     return df


def setCandlesInterval():
    interval = input("Set candle interval: ")   
    interval = int(interval)
    data = getCandles()
    df = pd.DataFrame([x.as_dict() for x in data])
    for i in range(0, len(df), interval):
        ci = df[i:i+interval].max()
    return ci

def getCandlesInterval():
    print(setCandlesInterval())


# while True:
#     getCandles()
#     getCandlesInterval()