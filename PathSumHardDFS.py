class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(5)
root.left = Node(4)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right = Node(8)
root.right.left = Node(13)
root.right.right = Node(4)

def hasPathSum(node, target):

    if not node:
        return False
    
    remaining = target - node.value

    if not node.left and not node.right:
        return remaining == 0
    
    left = hasPathSum(node.left, remaining)
    right = hasPathSum(node.right, remaining)

    return left or right

print(hasPathSum(root, 22))
