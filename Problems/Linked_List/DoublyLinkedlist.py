class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        

class MyLinkedList:
    def __init__(self):
        self.head=Node(0)
        self.tail=Node(0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size = 0

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index-=1
        if cur and cur != self.tail and index == 0:
            return cur.val
        else:
            return -1

        

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.head.next
        newnode.prev = self.head
        self.head.next = newnode
        newnode.next.prev = newnode
        self.size+=1

        

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.tail
        newnode.prev = self.tail.prev
        self.tail.prev.next = newnode
        self.tail.prev = newnode
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        newnode = Node(val)
        cur = self.head.next
        i=0

        while cur != self.tail and i < index:
            cur = cur.next
            i+=1

        if i != index:
            return

        newnode.next = cur
        newnode.prev = cur.prev
        cur.prev.next = newnode
        cur.prev = newnode
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.head.next
        i=0
        while i < index:
            cur = cur.next
            i+=1
        
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.size-=1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)