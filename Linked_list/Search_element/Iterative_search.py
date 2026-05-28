class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search_element(head, target):
    current_node = head
    while current_node is not None:
        if current_node.data == target:
            return True
        current_node = current_node.next
    return False

first_node = Node(10)
second_node = Node(20)
third_node = Node(30)
fourth_node = Node(40)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

head = first_node

target = int(input("Enter element to search: "))

result = search_element(head, target)

if result:
    print("Element Found")
else:
    print("Element Not Found")