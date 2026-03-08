class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)

def sumTree(node):

    if not node:
        return 0
    
    left = sumTree(node.left)

    right = sumTree(node.right)

    return node.value + left + right

print(sumTree(root))