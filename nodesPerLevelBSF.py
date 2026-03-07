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
root.left.right = Node(5)
root.right.right = Node(6)

def nodesPerLevel(root):

    if not root:
        return 

    queue = deque([root])
    result = []

    while queue:

        levelSize = len(queue)
        levelSizeList = []

        for _ in range(levelSize):
            node = queue.popleft()
            levelSizeList.append(node.value)
            
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        
        result.append(len(levelSizeList))
    return result

print(nodesPerLevel(root))