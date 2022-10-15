class Node: 
    def __init__(self, value=None):
        self.value = value 
        self.next = None 

class SLinkedList:
    def __init__(self, value=None):
        self.head  = Node(value)
        self.tail = self.head 
    

    def addAtHead(self, value):
        newNode = Node(value)
        currNode = self.head 
        newNode.next = currNode
        self.head = newNode 

    def removeAthead(self):
        newNode = self.head.next 
        self.head = newNode


    def __repr__(self):
        currNode = self.head 
        arr = []
        while currNode != None: 
            arr.append(str(currNode.value))
            currNode = currNode.next 
        return "->".join(arr)

    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode 
        self.tail  = newNode 

sLinkedList = SLinkedList(10)
sLinkedList.append(1)
sLinkedList.addAtHead(2)
sLinkedList.removeAthead()
print(sLinkedList)
    