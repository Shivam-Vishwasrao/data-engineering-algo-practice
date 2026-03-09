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

def maxValue(node):

    if not node:
        return float("-inf") # 0 will break tree with -ve #'s
    
    leftMax = maxValue(node.left)
    rightMax = maxValue(node.right)

    return max(node.value, leftMax, rightMax)

print(maxValue(root))