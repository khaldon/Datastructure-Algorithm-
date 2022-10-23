class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
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
                currNode.next = temp.next
                return
            currNode = currNode.next
            temp = temp.next

    def reverse(self):
        prev = None
        arr = []
        while self.head:
            currNode = self.head
            self.head = self.head.next
            currNode.next = prev
            prev = currNode
        currNode = prev
        while currNode != None:
            arr.append(str(currNode.value))
            currNode = currNode.next
        return "->".join(arr)

    def length(self):
        currNode = self.head
        count = 0
        while currNode != None:
            count += 1
            currNode = currNode.next
        return count

    def getMiddleNode(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
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
        self.tail = newNode

    def insert(self, index, value):
        new_node = Node(value)
        curr_node = self.head
        count = 0
        while curr_node:
            if count == index - 1:
                temp = curr_node.next
                new_node.next = temp
                curr_node.next = new_node
            count += 1
            curr_node = curr_node.next


sLinkedList = SLinkedList(10)
sLinkedList.append(1)
sLinkedList.addAtHead(2)
sLinkedList.addAtHead(2)
sLinkedList.addAtHead(2)

sLinkedList.removeAthead()
sLinkedList.remove(1)
# print(sLinkedList.getMiddleNode())
# print(sLinkedList.reverse())
print(sLinkedList)
