class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

# We are searching for the depth of the tree - so, process children first (left and right) 
# subtree and then come back to root node finally.

def maxDepth(node):

    if not node:
        return 0

    # process left tree
    leftDepth = maxDepth(node.left)
    # process right tree
    rightDepth = maxDepth(node.right)

    # compute depth
    return 1 + max(leftDepth, rightDepth) # '1' is for parent node

print(maxDepth(root))