import pandas as pd

class DF(pd.myObject):
    def __init__(self, pos, data):
        self.pos = pos
        self.data = data

    def __str__(self):
        return "pos: {}, data: {}".format(self.pos, self.data)

    def __repr__(self):
        return self.__str__()