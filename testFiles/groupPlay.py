import pandas as pd
import numpy as np
import threading
import time

# Shared flag to control the threads
stop_flag = False

df = pd.DataFrame()
df2 = pd.DataFrame()
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
    while not stop_flag:
        time.sleep(1) 
        global df
        df = pd.concat([df, makeKline()], ignore_index=True)  
        if len(df) > 10:
            df = df.iloc[1:]
        print("\n 1 Minute Klines \n")
        print(df) 

def timedKline():
    df3 = pd.DataFrame()
    for i in range(0, len(df) - (len(df) % 4), 4): # adjust range to avoid remainder rows 
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

def getUserKline():
    while not stop_flag:
        time.sleep(4) 
        global df2
        df2= pd.concat([df2, timedKline()], ignore_index=True) 
        print("Please hit!")
        print(df2)


def quitThreads():
    global stop_flag
    while not stop_flag:
        execute = input("Press Q to quit: \n")
        if execute == "q":
            print("goodbye")
            stop_flag = True
            thread1.join()
            thread2.join()


# The following code can be used to concat getUserKline() to a new pandas dataframe: 
# df_new = pd.DataFrame()
# while not stop_flag: 
#     df_temp = getUserKline() 
#     df_new = pd.concat([df_new, df_temp], ignore_index=True) 
# print(df_new)
  
# Start the threads
thread1 = threading.Thread(target=klines1Min)
thread2 = threading.Thread(target=getUserKline)
thread3 = threading.Thread(target=quitThreads)
thread1.start()
thread2.start()
thread3.start()


