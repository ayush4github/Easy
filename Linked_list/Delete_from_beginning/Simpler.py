#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def delete_from_beginning(head):
    #Empty List
    if head is None:
        print("Linked list is empty")
        return None
    #Store old head
    deleted_node = head
    #Move head
    head = head.next
    print("Deleted node=", deleted_node.data)
    return head