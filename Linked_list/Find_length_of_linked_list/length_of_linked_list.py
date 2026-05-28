#Class Node
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
#Head
head = first_node
#Print Linked List
current_node = head
while current_node is not None:
    print(current_node.data, end = "->")
    current_node = current_node.next
print("None")
#Find Length
length = 0
current_node = head
while current_node is not None:
    length +=1
    current_node = current_node.next
#Output
print("Length = ", length)