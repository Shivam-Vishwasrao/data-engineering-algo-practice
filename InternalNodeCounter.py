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

# internal nodes - node w atleast 1 child

def internalNodeCounter(node):

    if not node:
        return 0

    count = 0
    if (not node.left and node.right) or (not node.right and node.left) or (node.left and node.right):
        count += 1

    left = internalNodeCounter(node.left)
    right = internalNodeCounter(node.right)

    return count + left + right

print(internalNodeCounter(root))