class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(5)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(1)

def countSingleChild(node):

    if not node:
        return 0
    
    count = 0

    if (node.left and not node.right) or (node.right and not node.left):
        count += 1

    leftTree = countSingleChild(node.left)
    rightTree = countSingleChild(node.right)

    return count + leftTree + rightTree # (+) because we are counting nodes

print(countSingleChild(root))