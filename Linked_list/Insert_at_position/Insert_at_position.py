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
#Connect nodes
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
#Create new node
new_node = Node(25)
#Insert between 20 and 30
second_node.next = new_node
new_node.next = third_node
#Print linked list
current_node = first_node
while current_node is not None:
    print(current_node.data, end="->")
    current_node = current_node.next
print("None")