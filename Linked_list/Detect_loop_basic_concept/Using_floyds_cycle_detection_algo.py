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
#Connect Nodes
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
#Create Loop
fourth_node.next = second_node
#Slow Pointer
slow_pointer = first_node
#Fast Pointer
fast_pointer = first_node
#Detect loop
while fast_pointer is not None and fast_pointer.next is not None:
    slow_pointer = slow_pointer.next
    fast_pointer = fast_pointer.next.next
    if slow_pointer == fast_pointer:
        print("Loop Detected")
        break
