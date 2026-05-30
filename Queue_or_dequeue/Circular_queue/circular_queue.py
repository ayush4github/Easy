class CircularQueue:
    def __init__(self, size):
        self.queue = [None]*size
        self.size = size
        self.front = -1
        self.rear = -1
    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            return "Queue Full"
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear +1) % self.size
        self.queue[self.rear] = value
    def dequeue(self):
        if self.front == -1:
            return "Queue Empty"
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear =-1
        else:
            self.front = (self.front +1)% self.size
        return value
#Driver Code
queue = CircularQueue(3)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue()) #10
queue.enqueue(40)
print(queue.queue)