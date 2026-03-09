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

def countGreater(node, x):

    if not node:
        return 0
    
    count = 0
    
    if node.value > x:
        count += 1

    leftCount = countGreater(node.left, x)
    rightCount = countGreater(node.right, x)

    return count + leftCount + rightCount

print(countGreater(root, 3))