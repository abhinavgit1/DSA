class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        # Create first node
        node = Node(homepage)
        node.prev = self.head
        node.next = self.tail
        self.head.next = node
        self.tail.prev = node

        self.cur = node  # current page

    def visit(self, url: str) -> None:
        # Cut forward history
        self.cur.next = self.tail
        self.tail.prev = self.cur

        # Create and insert new node
        newnode = Node(url)
        newnode.prev = self.cur
        newnode.next = self.tail
        self.cur.next = newnode
        self.tail.prev = newnode
        self.cur = newnode

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.prev != self.head:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next != self.tail:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
