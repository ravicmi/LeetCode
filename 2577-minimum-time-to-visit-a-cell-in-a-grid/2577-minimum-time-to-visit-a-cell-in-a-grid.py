class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        import heapq
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        dir = [(-1,0), (1,0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        visited = dict()
        # visited[(0,0)] = 0 
        heap = []
        heapq.heappush(heap, (0, 0, 0))
        while heap:
            t, r, c = heapq.heappop(heap)
            if (r,c) not in visited : 
                visited[(r,c)] = t
                for dr, dc in dir: 
                    if (r+dr >=0) and (r+dr <m )and (c+dc >= 0) and (c+dc <n) and (r+dr, c+dc) not in visited: 
                        if grid[r+dr][c+dc] <= t+1:
                            heapq.heappush(heap, (t+1, r+dr , c+dc))
                        elif (grid[r+dr][c+dc] - t) % 2 != 0 : 
                            heapq.heappush(heap, (grid[r+dr][c+dc], r+dr , c+dc))
                        else: 
                            heapq.heappush(heap, (grid[r+dr][c+dc]+1, r+dr , c+dc))

        return visited[(m-1, n-1)]


        


