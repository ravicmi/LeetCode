class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        min_heap = []
        heap_len = 0
        for i in nums: 
            heapq.heappush(min_heap, i)
            heap_len +=1
            if len(min_heap) > k: 
                heapq.heappop(min_heap)
        return min_heap[0]
