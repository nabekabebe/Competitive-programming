class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        heappush(self.left, -1*num)
        heappush(self.right, -1*heappop(self.left))
        
        if len(self.right) > len(self.left):
            heappush(self.left, -1*heappop(self.right))
            
    def findMedian(self) -> float:
        if len(self.left)  == len(self.right):
            return (self.right[0] + -self.left[0]) / 2 
        else:
            return -1*self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
