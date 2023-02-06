import pandas as pd
import numpy as np
import threading
import time
import sys

df = pd.DataFrame()

def createCandle():
    n = 10
    data = np.random.randint(0, 10, size=(n, 4))
    df = pd.DataFrame(data, columns=['open', 'high', 'low', 'close'])
    endRow = df.shape[0]
    closeFix = df["close"][endRow - 1]
    openFix = df["open"][0]
    highFix = df["high"].max()
    lowFix= df["low"].min()
    dfFix = pd.DataFrame({'open': [openFix], 'high': [highFix], 'low': [lowFix], 'close': [closeFix]})
    # print("\nOriginal DF\n")
    # print(df)
    # print("\n Update DF \n")
    # print(dfFix)
    return dfFix

def createCandleThread(): 
    while True: 
        global df
        df = pd.concat([df, createCandle()], ignore_index=True)  
        if len(df) > 10:
            df = df.iloc[1:]
        print("\n")
        print(df) 
        time.sleep(3) 

def quitThread():
    while True:
        execute = input("Press Q to quit: ")
        if execute == "q":
            print("goodbye")
            sys.exit()

  
t1 = threading.Thread(target=createCandleThread) 
t1.daemon=True
t2 = threading.Thread(target=quitThread).start() 
t1.start() 
