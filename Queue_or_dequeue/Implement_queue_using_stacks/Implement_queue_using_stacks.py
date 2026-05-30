class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, value):
        self.stack1.append(value)
    def dequeue(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) ==0:
            return "Queue is Empty"
        return self.stack2.pop()
#Driver Code
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())
print(queue.dequeue())