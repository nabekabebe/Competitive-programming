class MyQueue:
    def __init__(self):
        self.one = []
        self.two = []
        self.top = None
    def push(self, x: int) -> None:
        self.one.append(x)
        self.top = self.one[0]
        
    def pop(self) -> int:
        while self.one:
            self.two.append(self.one.pop())
        val = self.two.pop()
        
        self.top = None if len(self.two) == 0 else self.two[len(self.two) -1]
        
        while self.two:
            self.one.append(self.two.pop())
        return val
    
    def peek(self) -> int:
        if len(self.one) == 0:
            return None
        else:
            return self.top
        
    def empty(self) -> bool:
        return len(self.one) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
