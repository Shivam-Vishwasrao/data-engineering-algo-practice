class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)

def lowestCommonAncestor(node, p, q):
    
    if not node:
        return 0
    
    if node.value == p or node.value == q:
        return node.value

    left = lowestCommonAncestor(node.left, p, q)
    right = lowestCommonAncestor(node.right, p, q)

    if left and right:
        return node.value
    
    return left or right

print(lowestCommonAncestor(root, 7, 4))
