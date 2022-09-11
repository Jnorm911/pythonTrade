class myObject:
    def __init__(self, pos, data):
        self.pos = pos
        self.data = data

    def __str__(self):
        return "pos: {}, data: {}".format(self.pos, self.data)

    def __repr__(self):
        return self.__str__()

    def as_dict(self):
        return {'pos': self.pos, 'data': self.data}