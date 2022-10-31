import random
import time
import numpy as np
import pandas as pd
from object import myObject
from counter import *

no = 0
number = Counter()
bucketSize = 5
instanceList = []

def getData():
    data = random.randint(0, 9)
    return data


def createObject():
    data = getData()
    instance = myObject(no, data)
    object2list(instance)


def object2list(instance):
    instanceList.append(instance)
    if len(instanceList) > 41:
        del instanceList[0]
    list2df()


def list2df():
    df = pd.DataFrame([x.as_dict() for x in instanceList])
    number.increment()
    bucketSize = int(str(number))
    if bucketSize >= 5:
        number.decrement(5)
        df2 = df.groupby(np.arange(len(df)) // 5).agg(lambda x: x.mode().to_numpy()[-1]) 
        print("\nAverage of 5\n")
        print(df2)
    else:
        print(df)
    return df


def getDf():
    return list2df()


while True:   
    createObject()
    time.sleep(3)
    getDf()

