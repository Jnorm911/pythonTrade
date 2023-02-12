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

# Function
# For every 4 rows of klines make a pandas dataframe

