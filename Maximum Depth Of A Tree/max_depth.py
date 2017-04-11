class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.height = 0
        self.value = value

def buildTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(6)
    root.left.left = Node(4)
    root.left.left.left = Node(5)
    return root

def findDepth(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        root.height = 0
    else:
        findDepth(root.left)
        findDepth(root.right)
        if root.left is not None and root.right is not None:
            root.height = max(root.left.height,root.right.height) + 1
        elif root.left is not None:
            root.height = root.left.height + 1
        else:
            root.height = root.right.height + 1
    return


def main():
    root = buildTree()
    findDepth(root)
    print(root.height)

if __name__ == '__main__':
    main()
