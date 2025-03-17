class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        pq = [(x*x+y*y, [x,y]) for x,y in points]
        heapq.heapify(pq)
        result = []
        for i in range(k):
            _, point = heapq.heappop(pq)
            result.append(point)
        return result