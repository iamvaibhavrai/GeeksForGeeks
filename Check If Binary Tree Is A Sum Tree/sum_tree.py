class Node():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def isSumTree(root):
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return root.value == root.right.value + root.left.value
    if root.left is not None:
        return root.value == root.left.value
    if root.right is not None:
        return root.value == root.right.value

def main():
    root = Node(10)
    root.left = Node(6)
    root.left.left = Node(4)
    root.left.right = Node(2)
    root.right = Node(4)
    root.right.left = Node(1)
    root.right.right = Node(3)
    if isSumTree(root):
        print("This binary tree is sum tree.")
    else:
        print("This binary tree is not a sum tree.")

if __name__ == '__main__':
    main()
