from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

def minDepth(root):

    if not root:
        return 0

    depth = 0
    queue = deque([root])

    while queue:

        depth += 1
        levelSize = len(queue)

        for _ in range(levelSize):
            node = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

    return depth

print(minDepth(root))