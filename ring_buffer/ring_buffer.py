class RingBuffer:
    """ class that implements a not-yet-full buffer """
    def __init__(self, capacity):
        self.capacity = capacity        
        self.data = []
        self.cur = 0

    def append(self,x):
        """append an element at the end of the buffer"""
        if len(self.data) < self.capacity:
            self.data.append(x)
        else:
            self.data[self.cur] = x

        self.cur = (self.cur+1) % self.capacity

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data







