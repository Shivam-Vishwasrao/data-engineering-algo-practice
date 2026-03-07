from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.right.right = Node(4)

def rightViewBFS(root):

    if not root:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        levelSize = len(queue)
        runningTotal = 0
        
        for i in range(levelSize):
            # dequeu node
            node = queue.popleft()

            # process node
            if i == levelSize - 1:
                result.append(node.value)
            
            # check for children
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
    
    return result

print(rightViewBFS(root))
