class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(5)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(1)

def countNodes(node):

    if not node:
        return 0

    left = countNodes(node.left)
    right = countNodes(node.right)

    return 1+left+right # 1 b'coz postOrder traversal (1 counts root node)

print(countNodes(root))

# NODES GREATER THAN TARGET VARIATION
# def countNodes(node, target):

#     if not node:
#         return 0
    
#     count = 0

#     if node.value > target:
#         count += 1

#     left = countNodes(node.left, target)
#     right = countNodes(node.right, target)

#     return count + left + right

# print(countNodes(root, 3))