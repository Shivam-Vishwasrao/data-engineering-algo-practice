class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)

def inOrderTraversal(node, result):

    if not node:
        return 
    
    inOrderTraversal(node.left, result)

    result.append(node.value)

    inOrderTraversal(node.right, result)

    return result

print(inOrderTraversal(root, []))

