from collections import deque

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

def averagePerLevel(root):

    if not root:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        levelSize = len(queue)
        runningSum = 0

        for _ in range(levelSize):

            node = queue.popleft()
            runningSum += node.value

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(runningSum / levelSize)
    
    return result

print(averagePerLevel(root))