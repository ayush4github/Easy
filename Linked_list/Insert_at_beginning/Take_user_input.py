class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def traverse_linked_list(head):
    current_node = head
    while current_node.next is not None:
        current_node = current_node.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

value = int(input("Enter value to insert: "))

head = insert_at_beginning(head, value)

traverse_linked_list(head)