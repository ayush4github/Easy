#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#Remove Duplicates
def remove_duplicates(head):
    #Empty Linked List:
    if head is None:
        return None
    #Start Traversal
    current_node = head
    #Traverse Linked List
    while current_node.next is not None:
        #Duplicate Found
        if current_node.data == current_node.next.data:
            #Skip Duplicate Node
            current_node.next = current_node.next.next
        else:
            #Move Forward
            current_node = current_node.next
    return head
#Traverse Linked List
def traverse_linked_list(head):
    current_node = head
    while current_node is not None:
        print(current_node.data, end = "->")
        current_node = current_node.next
    print("None")
# Create Linked List
first_node = Node(10)
second_node = Node(20)
third_node = Node(20)
fourth_node = Node(30)
fifth_node = Node(30)
sixth_node = Node(40)

# Connect Nodes
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node
fifth_node.next = sixth_node

# Head
head = first_node

print("Before Removing Duplicates:")
traverse_linked_list(head)

# Remove Duplicates
head = remove_duplicates(head)

print("After Removing Duplicates:")
traverse_linked_list(head)