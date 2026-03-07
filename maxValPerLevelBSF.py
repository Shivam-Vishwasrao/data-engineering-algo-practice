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

def maxValPerLevel(root):

    if not root:
        return []
    
    # initialize queue
    queue = deque([root])
    result = []
    
    # While queue is not empty
    while queue:
        # Get total # of nodes per level
        levelSize = len(queue)
        currentMax = float("-inf")

        for _ in range(levelSize):
            node = queue.popleft()
            if node.value > currentMax:
                currentMax = node.value

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
            
        result.append(currentMax)
    return result

print(maxValPerLevel(root))