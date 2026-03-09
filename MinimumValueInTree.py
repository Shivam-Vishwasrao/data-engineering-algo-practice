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

def minimumValue(node):

    if not node:
        return float("inf")

    leftMinimum = minimumValue(node.left)
    rightMinimum = minimumValue(node.right)

    return min(node.value, leftMinimum, rightMinimum)

print(minimumValue(root)) 