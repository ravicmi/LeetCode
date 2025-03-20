class MedianFinder:
    from heapq import heappop, heappush
    def __init__(self):        
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heappush(self.left, -num)
        if self.left and self.right and -self.left[0] > self.right[0]:
            heappush(self.right, -heappop(self.left))
        
        if len(self.left) > len(self.right)+1:
            heappush(self.right, -heappop(self.left))
        elif len(self.left) < len(self.right):
            heappush(self.left, -heappop(self.right))
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0]+self.right[0])/2    
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()