#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#Create linked list
first_node = Node(10)
second_node = Node(20)
third_node = Node(30)
#Connect Nodes
first_node.next = second_node
second_node.next = third_node
#Create New Node
new_node = Node(40)
#Insert at End
third_node.next = new_node
#Print Linked List
current_node = first_node
while current_node is not None:
    print(current_node.data, end="->")
    current_node = current_node.next
print("None")