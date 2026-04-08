class FreqStack:
    import heapq 
    from collections import defaultdict
    def __init__(self):
        # self.pos_dict = defaultdict(list)
        self.freq = defaultdict(int)
        self.maxheap = []  
        self.size = 0     

    def push(self, val: int) -> None:
        self.freq[val] +=1
        heapq.heappush(self.maxheap, (-self.freq[val], -self.size, val))
        # print('pushed', val)
        # print(self.maxheap)
        self.size +=1

        

    def pop(self) -> int:
        _ , _, val = heapq.heappop(self.maxheap)
        self.freq[val] -=1
        # print('popped')
        # print(self.maxheap)
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()