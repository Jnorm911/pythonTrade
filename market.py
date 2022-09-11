import time
 
from kucoin.client import Market
from candle import Candle

client = Market(url="https://api.kucoin.com")
current_time = client.get_server_timestamp()
no = 0
color = None
duration = 1


def counter(num):
    num += 1
    return num


def setColor(color):
    if no == 1:
        color = "R"
    else:
        color = "G"
    return color


def makeFirstCandle():
    klines = client.get_kline("KCS-USDT", "1min")
    df = pd.DataFrame(
        klines, columns=["start", "open", "close", "high", "low", "volume", "amount"]
    )
    no = 0
    color = None
    endRow = df.shape[0]
    openAH = df["open"][0]
    highAH = df["high"].max()
    lowAH = df["low"].min()
    closeAH = df["close"][endRow - 1]
    voluemAH = "{:.2f}".format(df["volume"].astype(float).sum())
    candle = Candle(no, duration, color, openAH, highAH, lowAH, closeAH, voluemAH)
    print(candle)
    return candle


def makeCandle():
    klines = client.get_kline("KCS-USDT", "1min")
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
    print(candle)
    return candle


# print(df)
# print('Open:  ', openAH)
# print('High:  ', highAH)
# print('Low:   ', lowAH)
# print('Close: ', closeAH)
# print('volume: ', voluemAH)

# closePrice = (openAH + highAH + lowAH + closeAH) / 4

makeFirstCandle()
time.sleep(60)

while True:
    no += 1
    color = setColor(color)
    makeCandle()
    time.sleep(60)
