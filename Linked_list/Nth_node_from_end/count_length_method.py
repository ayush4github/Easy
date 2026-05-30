#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def nth_node_from_end(head, position_from_end):
    #Find Length
    length = 0
    current_node = head
    while current_node is not None:
        length +=1
        current_node = current_node.next
        #Invalid Position
        if position_from_end > length:
            return None
        #Target Position from Start
        target_position = length - position_from_end
        current_node = head
        #Traverse to Target
        for current_position in range(target_position):
            current_node = current_node.next
        return current_node