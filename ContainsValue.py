class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(5)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(1)

def containsValue(node, target):

    if not node:
        return False
    
    if node.value == target:
        return True
    
    leftTree = containsValue(node.left, target)
    rightTree = containsValue(node.right, target)

    # This is same as:

    # if leftTree or rightTree:
    #     return True
    # return False

    # This:
    return leftTree or rightTree

print(containsValue(root, 1))