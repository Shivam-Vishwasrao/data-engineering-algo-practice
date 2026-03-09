class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(5)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(4)

def treeHeight(node):

    if not node:
        return 0
    
    leftHeight = treeHeight(node.left)
    rightHeight = treeHeight(node.right)

    return 1 + max(leftHeight, rightHeight)

print(treeHeight(root))
