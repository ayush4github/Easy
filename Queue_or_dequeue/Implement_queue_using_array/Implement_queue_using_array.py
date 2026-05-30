class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is Empty"
        return self.queue.pop(0)
    def front(self):
        if len(self.queue) == 0:
            return "Queue is Empty"
        return self.queue[0]
#Driver Code
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front Element: ", queue.front())
print("Dequeued: ", queue.dequeue())
print("Front Element After Dequeue: ", queue.front())