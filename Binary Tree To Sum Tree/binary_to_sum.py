class Node():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def binaryToSumTree(root):
    if root.left is None and root.right is None:
        temp = root.value
        root.value = 0
        return temp
    if root.left is not None and root.right is not None:
        root.value += binaryToSumTree(root.left) + binaryToSumTree(root.right)
        return root.value
    if root.left is not None:
        root.value += binaryToSumTree(root.left)
        return root.value
    if root.right is not None:
        root.value += binaryToSumTree(root.right)
        return root.value

def printTree(root):
    if root is None:
        return
    if root.left is not None:
        print(root.left.value)
    if root.right is not None:
        print(root.right.value)
    printTree(root.left)
    printTree(root.right)

def main():
    root = Node(10)
    root.left = Node(-2)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    root.right = Node(6)
    root.right.left = Node(7)
    root.right.right = Node(5)
    root.value = 0
    binaryToSumTree(root)
    print(root.value)
    printTree(root)

if __name__ == '__main__':
    main()
