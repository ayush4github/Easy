#Create Node Class
class Node:
    def __init__(self, data):
        #Store value
        self.data = data
        #Next node initially none
        self.next = None
#Create Nodes
first_node = Node(10)
second_node = Node(20)
third_node = Node(30)
#Connect nodes
first_node.next = second_node
second_node.next = third_node
#Insert new node at end
new_node = Node(40)
third_node.next = new_node
#Print linked list
current_node = first_node
while current_node is not None:
    print(current_node.data, end="->")
    current_node = current_node.next
print("None")