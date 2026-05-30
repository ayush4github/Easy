#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#Create Nodes
first_node = Node(10)
second_node = Node(20)
third_node = Node(30)
#Connect Nodes
first_node.next = second_node
second_node.next = third_node
#Create Loop
third_node.next = first_node
#Store Visited Nodes
visited_nodes = set()
#Start Traversal
current_node = first_node
#Detect Loop
while current_node is not None:
    #Already Visited
    if current_node in visited_nodes:
        print("Loop Detected")
        break
    #Store Node
    visited_nodes.add(current_node)
    #Move Forward
    current_node = current_node.next