class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        if grid[n-1][n-1] !=0 or grid[0][0] != 0 : 
            return -1
        
        def neighbour(i,j):
            delta_list = [(-1,-1), (-1,0), (-1, 1)
                         ,(0,-1),          (0, 1)
                         ,(1,-1),  (1,0),  (1, 1)]
            neigh = [(i+di, j+dj) for (di, dj) in delta_list if 0<=(i+di)<n and 0<=(j+dj)<n ]
            return neigh
        bfs = deque()
        bfs.append((n-1, n-1, 1))
        grid[n-1][n-1] = 1
        
        while bfs: 
            a, b, distance = bfs.popleft()
            if a == 0 and b == 0 : 
                return distance
            neigh = neighbour(a,b)
            filtered_neigh = [(i,j) for (i,j) in neigh if grid[i][j]==0 ]
            for i,j in filtered_neigh:
                bfs.append((i , j, distance+1))
                grid[i][j] = 1
        return -1








        #     for (i,j) in bfs:
        #         if (i,j) == (0,0):
        #             return distance
        #         neigh = neighbour(i,j)
        #         new_neigh = [(i,j) for (i,j) in neigh if (grid[i][j]== 0) ]
        #         # temp.extend(new_neigh)
        #         for a in new_neigh:
        #             grid[i][j] = 1
        #             temp.append(a)
        #     bfs = temp
        #     distance +=1
        # return -1

