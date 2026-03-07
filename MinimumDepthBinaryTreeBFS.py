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
        return
    
    depth = 0
    nodesList = []

    queue = deque([root])

    while queue:
        levelSize = len(queue)
        depth += 1

        for _ in range(levelSize):
            node = queue.popleft()
            nodesList.append(node.value)
            
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

    print(nodesList)
    return depth

print(minDepth(root))
