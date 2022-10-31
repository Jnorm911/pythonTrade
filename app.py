from candleBase import startCandleBase
from candleInterval import getCandlesInterval
from threading import Thread
import sys

def exit():
    while True:
        execute = input("Press Q to quit: ")
        if execute == "q":
            print("goodbye")
            sys.exit()


# String for Kline Coin both sides i.e BTC-USDT #

# Candle interval #

# Strategy i.e Heiken Ashi etc #

# Candle coloring #

# Trade strategy #


t1 = Thread(target=startCandleBase, args=())
t2 = Thread(target=getCandlesInterval, args=())
t1.daemon=True
t1.start()
t2.start()
t3 = Thread(target=exit).start()

