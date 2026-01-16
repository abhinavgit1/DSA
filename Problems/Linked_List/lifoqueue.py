class MyStack:

    def __init__(self):
        self.queue = []
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        return self.queue.pop(-1)
        

    def top(self) -> int:
        return self.queue[-1]
        

    def empty(self) -> bool:
        if self.queue :
            return False
        else:
            return True
        