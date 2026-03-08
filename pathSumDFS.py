class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# root = Node(5)
# root.left = Node(4)
# root.right = Node(8)
# root.left.left = Node(11)
# root.left.left.left = Node(7)
# root.left.left.right = Node(2)
# root.right.left = Node(13)
# root.right.right = Node(4)

root = Node(4)
root.left = Node(6)
root.right = Node(4)

def pathSum(node, target):

    if not node:
        return False
    
    if not node.left and not node.right:
        return target == node.value
    
    target -= node.value

    leftSum = pathSum(node.left, target)
    rightSum = pathSum(node.right, target)

    if leftSum or rightSum:
        return True
    else:
        return False

print(pathSum(root, 10))
    
