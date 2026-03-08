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

def dfsPostOrderTraversal(node, result):

    if not node:
        return []
     
    dfsPostOrderTraversal(node.left, result)
    dfsPostOrderTraversal(node.right, result)

    result.append(node.value)

    return result

print(dfsPostOrderTraversal(root, []))