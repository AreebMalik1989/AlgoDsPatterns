class PriorityQueue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == []

    def insert(self, item):
        self.queue.append(item)

    def pop(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
