from object import myObject
import random
import time
import pandas as pd

no = -1
pos= "TBD"
data = None
instances = {}


def getData():
    data = random.randint(0,9)
    return data


def createObject():
    data = getData()
    instance = {'inst' + str(no): myObject(pos,data) }
    print(instance)
    getObjects(instance)

def getObjects(instance):
    instances.update(instance)
    #Control Stack Size works with Pandas
    # if len(instances) >= 5:
    #     (k := next(iter(instances)), instances.pop(k))
    # Test prints 
    # if(no==5):
    #     new_output = list(instances.values())
    #     print("\n")
    #     print(" all values in dictionary are:",new_output)
    #     print("\n")
    #     print(instances['inst6'])

while True:
    no+=1
    createObject()
    time.sleep(1)
    if(no==9):
        print("\n")
        break 

#print(instances['inst8'])

mySeries = pd.Series(instances)
print(mySeries)

