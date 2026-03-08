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

    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5

# DFS TRAVERSAL #1 - PREORDER (NODE -> LEFT -> RIGHT)
preOrderList = []
def preorder(node):
    if not node:
        return
    
    # print(node.value)
    preOrderList.append(node.value)
    preorder(node.left)
    preorder(node.right)

    return "PreOrder - ", preOrderList

print(preorder(root))

# DFS TRAVERSAL #2 - INORDER (LEFT -> NODE -> RIGHT)
inOrderList = []

def inOrder(node):
    if not node:
        return
    
    inOrder(node.left)
    inOrderList.append(node.value)
    inOrder(node.right)

    return "inOrderList - ", inOrderList

print(inOrder(root))

# DFS TRAVERSAL #3 - POSTORDER (LEFT -> RIGHT -> NODE)
postOrderList = []

def postOrder(node):

    if not node:
        return

    postOrder(node.left)
    postOrder(node.right)
    postOrderList.append(node.value)

    return "postOrderList - ", postOrderList

print(postOrder(root))