sumo=0
sume=0
class Node():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def printTree(root,dis):
    global sumo,sume
    if (dis%2) == 0:
        sume+=root.value
    else:
        sumo+=root.value
    if root.left != None:
        printTree(root.left,dis+1)
    if root.right != None:
        printTree(root.right,dis+1)
    return

def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)
    printTree(root,0)
    print(abs(sume-sumo))

if __name__ == '__main__':
    main()
