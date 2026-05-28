class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head
def traverse_linked_list(head):
    current_node = head
    while current_node is not None:
        print(current_node.data, end = "->")
        current_node = current_node.next
    print("None")

first_node = Node(10)
second_node = Node(20)
third_node = Node(30)
fourth_node = Node(40)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

head = first_node

print("Before insertion: ")
traverse_linked_list(head)

head = insert_at_beginning(head, 5)

print("After Insertion: ")
traverse_linked_list(head)