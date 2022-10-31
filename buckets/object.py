class object:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "data: {}".format(self.data)

    def __repr__(self):
        return self.__str__()

    def as_dict(self):
        return {'data': self.data}

    def as_int(self):
        return self.__int__()   