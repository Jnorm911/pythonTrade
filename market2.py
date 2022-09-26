from kucoin.client import Market
from candle import Candle

client = Market(url="https://api.kucoin.com")

klines = client.get_kline("KCS-USDT", "1min")
no=-1

Candle.makeCandles(no,klines)
