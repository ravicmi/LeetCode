class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        import heapq
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        dir = [(-1,0), (1,0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        visited = dict()
        min_times = [[float('inf')]*n for _ in range(m)]
        min_times[0][0] = 0
        heap = []
        heapq.heappush(heap, (0, 0, 0))
        while heap:
            t, r, c = heapq.heappop(heap)
            if r==m-1 and c==n-1:
                return t
            if (r,c) not in visited : 
                visited[(r,c)] = t
                for dr, dc in dir: 
                    nr , nc = r+dr, c+dc
                    if (nr>=0) and (nr<m )and (nc >= 0) and (nc <n) and (nr, nc) not in visited: 
                        if grid[nr][nc] <= t+1:
                            new_time = t+1
                        elif (grid[nr][nc] - t) % 2 != 0 : 
                            new_time = grid[nr][nc]
                        else: 
                            new_time = grid[nr][nc] +1
                        if new_time < min_times[nr][nc]:
                            heapq.heappush(heap, (new_time, nr, nc))

        return visited[(m-1, n-1)]


        


