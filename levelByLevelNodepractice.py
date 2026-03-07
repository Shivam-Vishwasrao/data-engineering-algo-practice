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
root.right.right = Node(5)

def bfs(root):

    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        levelSize = len(queue)
        level = []

        for _ in range(levelSize):
            node = queue.popleft()
            level.append(node.value)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        result.append(level)

    return result

print(bfs(root))

