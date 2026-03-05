from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Build the tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")

def bfs(root):
    # If empty return
    if not root:
        return
    
    # Add the root element to the queue
    queue = deque()
    queue.append(root)
    # queue = deque([root]) also gets the job done in 1 line

    while queue:
        node = queue.popleft()
        print(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
    
bfs(root)
        