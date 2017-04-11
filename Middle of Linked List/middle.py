class LinkedListNode:
    def __init__(self,value):
        self.next = None
        self.value = value

    def setValue(self,value):
        self.value = value

    def setNext(self,newNext):
        self.next = newNext

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

def builtList():
    head = LinkedListNode(1)
    node1 = LinkedListNode(2)
    node2 = LinkedListNode(3)
    node3 = LinkedListNode(4)
    node4 = LinkedListNode(5)
    node5 = LinkedListNode(6)
    head.setNext(node1)
    node1.setNext(node2)
    node2.setNext(node3)
    node3.setNext(node4)
    node4.setNext(node5)
    return head

def printList(head):
    node = head
    while node is not None:
        print(node.getValue())
        node = node.getNext()

def findMiddleNode(head):
    slow = fast = head
    while fast is not None and fast.getNext() is not None:
        slow = slow.getNext()
        fast = fast.getNext().getNext()
    return slow

def main():
    head = builtList()
    middle = findMiddleNode(head)
    print(middle.getValue())

if __name__ == '__main__':
    main()
