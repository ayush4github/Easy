class Stack:
    def __init__(self):
        self.queue = []
    def push(self, value):
        self.queue.append(value)
        #Move old elements behind new element
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
    def pop(self):
        if len(self.queue) == 0:
            return "Stack is Empty"
        return self.queue.pop(0)
    def peek(self):
        if len(self.queue) == 0:
            return "Stack is Empty"
        return self.queue[0]
#Driver Code
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top: ", stack.peek())
print("Popped: ", stack.pop())
print("Top After Pop: ", stack.peek())