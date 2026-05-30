#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#Find Nth node from end
def nth_node_from_end(head, position_from_end):
    #Empty Linked List
    if head is None:
        return None
    #First pointer
    first_pointer = head
    #Second_pointer
    second_pointer = head
    #Move First Pointer Ahead
    for current_position in range(position_from_end):
        #Position larger than length
        if first_pointer is None:
            return None
        first_pointer = first_pointer.next
        #Move both pointers
    while first_pointer is not None:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next
    return second_pointer
#Traverse Linked List
def traverse_linked_list(head):
    current_node = head
    while current_node is not None:
        print(current_node.data, end = "->")
        current_node = current_node.next
    print("None")
#Create Linked List
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
#Print Linked List
traverse_linked_list(head)
#Input
position_from_end = int(input("Enter position from end: "))
#Result
result = nth_node_from_end(head, position_from_end)
#Output
if result is not None:
    print("Nth node from end: ", result.data)
else:
    print("Invalid position")