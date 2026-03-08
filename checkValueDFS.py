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

def containsValue(node, target):

    if not node:
        return False
    
    # preOrder DFS, checking node first then branches
    if node.value == target:
        return True
    
    # Recursion on left and right branch
    leftBranch = containsValue(node.left, target)
    rightBranch = containsValue(node.right, target)

    if leftBranch or rightBranch:
        return True
    return False

print(containsValue(root, 6))