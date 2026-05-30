class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inorder(root):
    if root is None:
        return
    inorder(root.left)  #left
    print(root.data)    #root
    inorder(root.right) #right
#Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
inorder(root)