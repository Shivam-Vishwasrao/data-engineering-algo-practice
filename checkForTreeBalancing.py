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

def checkHeight(node):

    if not node:
        return 0
    
    left = checkHeight(node.left)
    if left == -1:
        return -1
    
    right = checkHeight(node.right)
    if right == -1:
        return -1
    
    if abs(left - right) > 1:
        return -1
    
    return 1 + max(left, right)

def isBalanced(root):
    return checkHeight(root) != -1

print(isBalanced(root))
    