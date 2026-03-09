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

def leafNodeCount(node):

    if not node:
        return 0

    count = 0

    if not node.left and not node.right:
        count += 1

    leftLeaf = leafNodeCount(node.left)
    rightLeaf = leafNodeCount(node.right)

    print(count)
    return count + leftLeaf + rightLeaf

print(leafNodeCount(root))