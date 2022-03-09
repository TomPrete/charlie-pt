class Queue:

    def __init__(self):
        self.base = []

    def enqueue(self, value):
        self.base.append(value)

    def dequeue(self):
        self.base.pop(0)

    def size(self):
        return len(self.base)

    def peek(self):
        return self.base[0]

queue = Queue()
queue.enqueue(3)
queue.enqueue(1)
queue.enqueue(4)
queue.enqueue(7)
print(queue.base)
queue.dequeue()
queue.dequeue()
print(queue.base)
print(queue.size())
print(queue.peek())

