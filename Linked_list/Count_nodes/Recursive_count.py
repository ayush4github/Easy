class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_nodes(head):
    if head is None:
        return 0
    return 1 + count_nodes(head.next)

first_node = Node(10)
second_node = Node(20)
third_node = Node(30)
fourth_node = Node(40)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

head = first_node

print("Number of nodes: ", count_nodes(head))