class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def search_element(head, target):
    if head is None:
        return  False
    if head.data == target:
        return True
    return search_element(head.next, target)

first_node = Node(10)
second_node = Node(20)
third_node = Node(30)
fourth_node = Node(40)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

head = first_node

target = int(input("Enter element: "))

if search_element(head, target):
    print("Element found")
else:
    print("Element Not found")