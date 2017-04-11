class LinkedListNode:
    def __init__(self,value,newNext=None):
        self.next = newNext
        self.value = value
    def add(self,value):
        self.next = None
        self.value = value

def buildList(a=0,b=0,c=0):
    node2 = LinkedListNode(c)
    node1 = LinkedListNode(b,node2)
    head = LinkedListNode(a,node1)
    return head

def addLists(node1,node2):
    carry = 0
    addition = 0
    result = buildList()
    temp = result
    while node1.next is not None and node2.next is not None:
        addition = node1.value + node2.value + carry
        carry = 1 if addition>9 else 0
        addition = addition % 10
        temp.value = addition
        temp = temp.next
        node1 = node1.next
        node2 = node2.next
    addition = node1.value + node2.value + carry
    temp.value = addition

    return result

def getNumber(head):
    node = head
    number = 0
    multiple = 1
    while node is not None:
        number += node.value * multiple
        multiple *= 10
        node = node.next
    return number

def main():
    node1 = buildList(2,3,5)
    node2 = buildList(8,8,5)
    result = addLists(node1,node2)
    number = getNumber(result)
    print(number)

if __name__ == '__main__':
    main()
