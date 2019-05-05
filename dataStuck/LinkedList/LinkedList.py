class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node()
    def add (self,data):
        if self.head.data == None:
            self.head.data = data
            return

        newNode = Node(data)
        iterator = self.head
        while iterator.next != None:
            iterator = iterator.next
        iterator.next = newNode
        self.size += 1
    
    def popLast(self):
        assert self.size != 0, "Can't pop empty LinkedList"
        iterator = self.head
        while iterator.next != None:
            prev = iterator
            iterator = iterator.next
        prev.next = None
        self.size -= 1
        return iterator.data
            

    def __repr__(self):
        iterator = self.head
        rv = ''
        while iterator != None:
            rv += str(iterator.data) + '->'
            iterator = iterator.next
        return rv

if __name__ == "__main__":
    myLinkedList = LinkedList()
    myLinkedList.add(12)
    myLinkedList.add(11)
    myLinkedList.add(19)
    # print(myLinkedList.popLast())
    myLinkedList.add(12)
    myLinkedList.add(13)
    print(myLinkedList)