class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def buildTree():
    root = Node(10)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(4)
    root.left.right = Node(8)
    return root

def printLeftBoundary(root):
    if root is not None:
        if root.left is not None:
            print(root.value)
            printLeftBoundary(root.left)
        elif root.right is not None:
            print(root.value)
            printLeftBoundary(root.right)

def printRightBoundary(root):
    if root is not None:
        if root.right is not None:
            printLeftBoundary(root.right)
            print(root.value)
        elif root.left is not None:
            printLeftBoundary(root.left)
            print(root.value)

def printLeaves(root):
    if root is not None:
        printLeaves(root.left)
        if root.left is None and root.right is None:
            print(root.value)
        printLeaves(root.right)

def printBoundary(root):
    printLeftBoundary(root)
    printLeaves(root.left)
    printLeaves(root.right)
    printRightBoundary(root.right)

def main():
    root = buildTree()
    printBoundary(root)

if __name__ == '__main__':
    main()
