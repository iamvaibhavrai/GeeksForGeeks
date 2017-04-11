class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def arrToBST(arr,root):
    if root is None:
        return
    arrToBST(arr,root.left)

    root.value = arr[0]
    arr.pop(0)

    arrToBST(arr,root.right)

def buildTree():
    root = Node(10)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(4)
    root.left.right = Node(8)
    return root

def inOrder(root,arr):
    if root is None:
        return
    inOrder(root.left,arr)
    arr.append(root.value)
    inOrder(root.right,arr)

def main():
    root = buildTree()
    arr = []
    inOrder(root,arr)
    arr.sort()
    arrToBST(arr,root)
    inOrder(root,arr)
    print(arr)


if __name__ == '__main__':
    main()
