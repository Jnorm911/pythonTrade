import pandas as pd
import numpy as np
import threading
import time
import sys

dfFixList = []
df = pd.DataFrame()

def createCandle():
    # Number of rows
    n = 10

    # Generate a numpy array with random numbers from 0 to 9
    data = np.random.randint(0, 10, size=(n, 4))

    # Convert numpy array to pandas DataFrame
    df = pd.DataFrame(data, columns=['open', 'high', 'low', 'close'])
    endRow = df.shape[0]
    closeFix = df["close"][endRow - 1]
    openFix = df["open"][0]
    highFix = df["high"].max()
    lowFix= df["low"].min()
    dfFix = pd.DataFrame({'open': [openFix], 'high': [highFix], 'low': [lowFix], 'close': [closeFix]})
    print("\nOriginal DF\n")
    print(df)
    print("\n Update DF \n")
    print(dfFix)
    return dfFix

def createCandleThread(): 
    while True: 
        global df
        df = df.append(createCandle(), ignore_index=True) 
        print(df) 
        time.sleep(5) 
  

def quitThread():
    while True:
        execute = input("Press Q to quit: ")
        if execute == "q":
            print("goodbye")
            sys.exit()

  
# Create the threads 
t1 = threading.Thread(target=createCandleThread) 
t1.daemon=True
t2 = threading.Thread(target=quitThread).start() 

# Start the threads 
t1.start() 
