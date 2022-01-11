class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.count = 0
        self.head = Node()
        self.tail = Node()
    
    def _initialize(self, node: Node):
        node.prev = self.head
        node.next = self.tail
        self.head.next = node
        self.tail.prev = node

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        if self.isEmpty():
            self._initialize(node)
        else:
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        if self.isEmpty():
            self._initialize(node)
        else:
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = self.tail.prev
        self.count -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.next.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.prev.val

    def isEmpty(self) -> bool:
        return not self.count

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
