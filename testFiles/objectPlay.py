import random
import time
import sys
import pandas as pd
from threading import Thread
from object import myObject

no = -1
pos = "TBD"
data = None
instances = []


def getData():
    data = random.randint(0, 9)
    return data


def createObject():
    data = getData()
    # dictionary with callable dynamic variable name
    instance = myObject(pos, data)
    getObjects(instance)


def getObjects(instance):
    instances.append(instance)
    # Control Stack Size works with Pandas
    if len(instances) > 41:
        del instances[0]
    updateObjects()


def updateObjects():
    df = pd.DataFrame([x.as_dict() for x in instances])
    dfData = df["data"]

    for i in range(len(dfData)):
        if i == 0:
            prevData = 0
            curData = dfData[i]
        else:
            prevData = df.iat[i - 1, 1]
            curData = dfData[i]
        if prevData < curData:
            df.loc[i, "pos"] = "High"
        elif prevData > curData:
            df.loc[i, "pos"] = "Low"
        else:
            df.loc[i, "pos"] = "Same"
    return df


def getDf():
    return updateObjects()


def startObject(no):
    while True:
        no += 1
        createObject()
        time.sleep(1)
        converted_num = str(no)
        if converted_num.endswith("0"):
            print("\nUpdated Dictionary\n")
            print(getDf())


def exit():
    while True:
        execute = input("Press Q to quit: ")
        if execute == "q":
            print("goodbye")
            sys.exit()




t1 = Thread(target=startObject, args=(no,))
t1.daemon=True
t1.start()
t2 = Thread(target=exit).start()


# print(instances['inst8'])

# df = pd.DataFrame([x.as_dict() for x in instances])
# df['data'] = df['data'].diff()
# print(df)

# Set candle color from Dictionary
# df = pd.DataFrame([x.as_dict() for x in instances])
# dfData = df['data']

# for i in range(len(dfData)):
#     if i == 0:
#         prevData = 0
#         curData = dfData[i]
#     else:
#         prevData = df.iat[i-1,1]
#         curData = dfData[i]
#     if(prevData < curData):
#         df.loc[i,'pos']="High"
#     elif(prevData > curData):
#         df.loc[i,'pos']="Low"
#     else:
#         df.loc[i,'pos']="Same"
