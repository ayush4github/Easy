#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#Stack Class
class Stack:
    def __init__(self):
        self.top = None
    #Push Operation
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    #Pop Operation
    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        popped_value = self.top.data
        self.top = self.top.next
        return popped_value
    #Peek Operation
    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.top.data
    #Check if Empty
    def is_empty(self):
        return self.top is None
    #Display Stack
    def display(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.data, end="->")
            current_node = current_node.next
        print("None")
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