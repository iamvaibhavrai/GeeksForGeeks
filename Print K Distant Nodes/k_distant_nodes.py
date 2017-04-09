class Node():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def printTree(root,dis,k):
    if dis == k:
        print(root.value)
        return
    if root.left != None:
        printTree(root.left,dis+1,k)
    if root.right != None:
        printTree(root.right,dis+1,k)
    return

def main():
    k = int(input())
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)
    printTree(root,0,k)

if __name__ == '__main__':
    main()
