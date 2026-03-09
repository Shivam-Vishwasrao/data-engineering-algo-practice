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

def leafSum(node):

    if not node:
        return 0
    
    sum = 0

    if not node.left and not node.right:
        sum += node.value

    leftTree = leafSum(node.left)
    rightTree = leafSum(node.right)

    return sum + leftTree + rightTree

print(leafSum(root))