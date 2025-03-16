class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        pq = []
        for x,y in points:
            distance = x*x + y*y
            pq.append((distance, x, y))
        heapq.heapify(pq)
        result = []
        for i in range(k):
            distance, x, y = heapq.heappop(pq)
            result.append([x,y])

        return result