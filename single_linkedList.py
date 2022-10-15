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


    def remove(self, value):
        currNode = self.head 
        temp = currNode.next 
        # 1 -> 2 -> 3 -> 4
        while True:
            if temp.value == value: 
                currNode.next  = temp.next
                return 
            currNode = currNode.next 
            temp = temp.next 
         



    
    def length(self): 
        currNode = self.head 
        count = 0 
        while currNode != None :
            count +=1 
            currNode  = currNode.next 
        return count 

    def getMiddleNode(self):
        slow = fast = self.head 
        while fast and fast.next:
            slow = slow.next 
            fast  = fast.next.next 
        currNode = slow  
        arr = []
        while currNode != None: 
            arr.append(str(currNode.value))
            currNode = currNode.next 
        return "->".join(arr)

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
sLinkedList.addAtHead(2)
sLinkedList.addAtHead(2)

sLinkedList.removeAthead()
sLinkedList.remove(1)
# print(sLinkedList.getMiddleNode())
print( sLinkedList)
    