class Queue:
    def __init__(self, maxSize=100):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.maxSize = maxSize
        self.storage = []

    def enqueue(self, item):
        if self.size == self.maxSize:
            return "Queue Full"
        else:
            self.storage.append(item)
            self.size = self.size + 1

    def dequeue(self):
        if len(self.storage) < 1:
            return None
        return self.storage.pop(0)

    def len(self):
        return len(self.storage)

