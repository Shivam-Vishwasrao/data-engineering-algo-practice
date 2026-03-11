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

Dia = 0

def diameter(node):
    global Dia

    if not node:
        return 0
    
    left = diameter(node.left)
    right = diameter(node.right)

    Dia = max(Dia, left + right)

    return 1 + max(left, right)

diameter(root)
print(Dia)
