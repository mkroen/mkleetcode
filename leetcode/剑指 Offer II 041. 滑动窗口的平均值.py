class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.count = 0
        self.sum = 0
        self.index = 0
        self.l = [0] * size

    def next(self, val: int) -> float:
        if self.count != self.size:
            self.count += 1
        self.sum -= self.l[self.index]
        self.l[self.index] = val
        self.sum += val
        self.index += 1
        self.index %= self.size
        return self.sum/self.count
