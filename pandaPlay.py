import pandas as pd
import random
import time
from object import myObject

no = -1
pos = "WiP"

def getData():
    data = random.randint(0,9)
    return data

def createObject():
    data = getData()
    instance = {'inst' + str(no): myObject(pos,data) }
    print(instance)
    getSeries(instance)

def getSeries(instance):
    mySeries = pd.Series(instance)
    if(no==5):
        print("\n")
        print(mySeries)



while True:
    no+=1
    createObject()
    time.sleep(1)
    if(no==5):
        print("\n")
        break 

