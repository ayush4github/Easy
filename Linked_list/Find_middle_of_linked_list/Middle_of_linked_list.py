#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#Create Nodes
first_node = Node(10)
second_node = Node(20)
third_node = Node(30)
fourth_node = Node(40)
fifth_node = Node(50)
#Connect Nodes
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node
#Head
head = first_node
#Print linked list
current_node = head
while current_node is not None:
    print(current_node.data, end = "->")
    current_node = current_node.next
print("None")
#Find Middle
slow_pointer = head
fast_pointer = head
while fast_pointer is not None and fast_pointer.next is not None:
    slow_pointer = slow_pointer.next
    fast_pointer = fast_pointer.next.next
#Output
print("Middle Node: ", slow_pointer.data)