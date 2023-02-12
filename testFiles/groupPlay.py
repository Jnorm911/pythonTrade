import pandas as pd
import numpy as np
import threading
import time
import sys

df = pd.DataFrame()
def makeKline():
    n = 10
    data = np.random.randint(0, 10, size=(n, 4))
    df = pd.DataFrame(data, columns=['open', 'high', 'low', 'close'])
    endRow = df.shape[0]
    closeFix = df["close"][endRow - 1]
    openFix = df["open"][0]
    highFix = df["high"].max()
    lowFix= df["low"].min()
    dfFix = pd.DataFrame({'open': [openFix], 'high': [highFix], 'low': [lowFix], 'close': [closeFix]})
    return dfFix
def klines1Min(): 
    while True: 
        time.sleep(1) 
        global df
        df = pd.concat([df, makeKline()], ignore_index=True)  
        if len(df) > 10:
            df = df.iloc[1:]
        print("\n 1 Minute Klines \n")
        print(df) 
def df2():
    df3 = pd.DataFrame()
    for i in range(0, len(df), 4):
        df4 = df.iloc[i:i+4]
        endRow = df4.shape[0]
        openFix = df4["open"].iloc[0]
        highFix = df4["high"].max()
        lowFix= df4["low"].min()
        closeFix = df4["close"].iloc[endRow - 1]
        df5 = pd.DataFrame({'open': [openFix], 'high': [highFix], 'low': [lowFix], 'close': [closeFix]})
        df3 = pd.concat([df3, df5], ignore_index=True) 
    print("\n 4 minute candle \n")
    print(df3)
    return df3

def quitThread():
    while True:
        execute = input("Press Q to quit: ")
        if execute == "q":
            print("goodbye")
            sys.exit()

  
t1 = threading.Thread(target=klines1Min) 
t1.daemon=True
t2 = threading.Thread(target=quitThread).start() 
t1.start() 

while True:
    time.sleep(10)
    df2()
# Function
# For every 4 rows of klines make a pandas dataframe

