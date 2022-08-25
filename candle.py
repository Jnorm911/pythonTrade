class Candle:
    def __init__(self, no, duration, color, op3n, high, low, close, volume):
        self.no = no
        self.duration = duration
        self.color = color
        self.op3n = op3n
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __str__(self):
        return ("Candle " + str(self.no) + " " + str(self.duration) + "min " + str(self.color) + " " + str(self.op3n) + " " + str(self.high) + " " + str(self.low) + " " + str(self.close) + " " + str(self.volume))
    def __repr__ (self):
        return self.__str__()