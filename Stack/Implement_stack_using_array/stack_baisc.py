class Stack:
    def __init__(self):
        self.stack = [] #Array (Python List)
        #Push element into stack
        def push(self, value):
            self.stack.append(value)
        #Pop element from stack
        def pop(self):
            if self.is_empty():
                return "Stack Underflow"
            return self.stack.pop()
        #Return top element
        def peek(self):
            if self.is_empty():
                return "Stack is Empty"
            return self.stack[-1]
        #Check if stack is empty
        def is_empty(self):
            return len(self.stack) == 0
        #Return size of stack
        def size(self):
            print(self.stack)
#Driver Code
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack: ")
stack.display()
print("Top Element: ", stack.peek())
print("Popped: ", stack.pop())
print("Stack After Pop: ")
stack.display()
print("Size: ", stack.size())