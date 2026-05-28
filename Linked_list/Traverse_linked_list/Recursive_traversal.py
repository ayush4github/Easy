class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_linked_list(head):
    if head is None:
        return
    print(head.data)
    traverse_linked_list(head.next)

first_node = Node(10)
second_node = Node(20)
third_node = Node(30)
fourth_node = Node(40)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

head = first_node

traverse_linked_list(head)