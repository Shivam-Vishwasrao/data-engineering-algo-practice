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

def sumOfNodes(node):

    if not node:
        return 0
    
    leftSum = sumOfNodes(node.left)
    rightSum = sumOfNodes(node.right)

    totalSum = node.value + leftSum + rightSum

    return totalSum
print(sumOfNodes(root))