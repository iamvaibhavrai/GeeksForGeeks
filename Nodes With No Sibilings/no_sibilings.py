class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def insertTree():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.left.left = Node(6)
    return root

def printNodesWithNoSibilings(root):
    if root is None:
        return

    if root.left is None and root.right is not None:
        print(root.right.value)
        printNodesWithNoSibilings(root.right)

    if root.right is None and root.left is not None:
        print(root.left.value)
        printNodesWithNoSibilings(root.left)

    if root.left is not None and root.right is not None:
        printNodesWithNoSibilings(root.left)
        printNodesWithNoSibilings(root.right)


def main():
    root = insertTree()
    printNodesWithNoSibilings(root)

if __name__ == '__main__':
    main()
