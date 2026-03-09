class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def countNodes(node):

    if not node:
        return 0
    
    leftNodeCount = countNodes(node.left)
    rightNodeCount = countNodes(node.right)

    return 1 + leftNodeCount + rightNodeCount

print(countNodes(root))