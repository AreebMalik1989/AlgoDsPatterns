class CircularQueue:

    def __init__(self, max_size):
        self.queue = list()
        self.max_size = max_size
        self.head = 0
        self.tail = 0

    def enqueue(self, item) -> bool:

        if self.size() == (self.max_size - 1):
            return False
        else:
            self.queue.append(item)
            self.tail = (self.tail+1) % self.max_size
            return True

    def dequeue(self):

        if self.size() == 0:
            return None
        else:
            item = self.queue[self.head]
            self.head = (self.head+1) % self.max_size
            return item

    def size(self):

        if self.tail >= self.head:
            size = self.tail - self.head
        else:
            size = self.max_size - (self.head - self.tail)

        return size
