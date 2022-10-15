class Node: 
    def __init__(self, value=None):
        self.value = value 
        self.next = None 

class SLinkedList:
    def __init__(self, value=None):
        self.head  = Node(value)
        self.tail = self.head 
    

    def append(self, value):
        newNode = Node(value)
        self.tail.next = NewNode 
        self.tail  = newNode 

    