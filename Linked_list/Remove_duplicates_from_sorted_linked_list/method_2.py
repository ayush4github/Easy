# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Recursive Duplicate Removal
def remove_duplicates(head):

    # Base Case
    if head is None or head.next is None:
        return head

    # Duplicate Found
    if head.data == head.next.data:

        # Skip Duplicate Node
        head.next = head.next.next

        # Check Again
        return remove_duplicates(head)

    # Recursive Call
    head.next = remove_duplicates(head.next)

    return head


# Traverse Linked List
def traverse_linked_list(head):

    current_node = head

    while current_node is not None:

        print(current_node.data, end=" → ")

        current_node = current_node.next

    print("None")


# Create Nodes
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


# Before Removing Duplicates
print("Before:")

traverse_linked_list(head)


# Remove Duplicates
head = remove_duplicates(head)


# After Removing Duplicates
print("After:")

traverse_linked_list(head)