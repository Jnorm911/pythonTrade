class Candle(dict):
    
    def __init__(self, duration, color, op3n, high, low, close, volume):
        self.duration = duration
        self.color = color
        self.op3n = op3n
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def get_duration(self):
        return self.duration

    def get_color(self):
        return self.color
    
    def get_open(self):
        return self.op3n

    def get_close(self):
        return self.close

    def get_high(self):
        return self.high

    def get_low(self):
        return self.low

    def get_volume(self):
        return self.volume

    def __str__(self):
        return ("Duration " + str(self.duration) + "min " + str(self.color) + " " + str(self.op3n) + " " + str(self.high) + " " + str(self.low) + " " + str(self.close) + " " + str(self.volume))
   
    def __repr__ (self):
        return self.__str__()

    def as_dict(self):
        return {'Duration': self.duration, 'Color': self.color, 'Open': self.op3n, 'High': self.high, 'Low': self.low, 'Close': self.close, 'Volume': self.volume}


