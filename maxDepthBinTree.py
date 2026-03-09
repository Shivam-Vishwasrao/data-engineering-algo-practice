class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

def maxDepth(node):

    if not node:
        return 0
    
    leftDepth = maxDepth(node.left)
    rightDepth = maxDepth(node.right)

    return 1 + max(leftDepth, rightDepth)
# Not sure where exactly should I update my depth.

print(maxDepth(root))
