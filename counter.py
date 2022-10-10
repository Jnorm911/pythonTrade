class Counter(object):
    def __init__(self):
        self.count = 0
        # initialize count at zero
    def increment(self, by=1):
        self.count += by
    def decrement(self, by=1):
        self.count -= by
    def __repr__(self):
            return(str(self.count))