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

def sumTree(node):

    if not node:
        return 0
    
    leftSum = sumTree(node.left)
    rightSum = sumTree(node.right)

    return node.value + leftSum + rightSum

print(sumTree(root))