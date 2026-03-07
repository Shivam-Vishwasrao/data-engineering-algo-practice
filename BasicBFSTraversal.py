from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root= Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

def simpleBSF(root):

    if not root:
        return []

    queue = deque()
    queue.append(root)
    result = []

    while queue:

        node = queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)

    return result

print(simpleBSF(root))