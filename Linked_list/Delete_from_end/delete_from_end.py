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
#Head
head = first_node
#Before Deletion
print("Before Deletion: ")
current_node = head
while current_node is not None:
    print(current_node.data, end = "->")
    current_node = current_node.next
print("None")
#Actual Deletion
third_node.next = None
#After Deletion
print("After Deletion: ")
current_node = head
while current_node is not None:
    print(current_node.data, end = "->")
    current_node = current_node.next
print("None")