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

def leafWithTarget(node, target):

    if not node:
        return False
    
    if (not node.left and not node.right):
        if node.value == target:
            return True
        return False
        
    leftTree = leafWithTarget(node.left, target)
    rightTree = leafWithTarget(node.right, target)

    return leftTree or rightTree

print(leafWithTarget(root, 4))