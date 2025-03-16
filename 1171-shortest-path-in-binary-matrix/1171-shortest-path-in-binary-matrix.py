class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:  
            return -1
        
        dist_dict = dict()
        
        
        def neighbour(i, j):
            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),         (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]
            return [(i + di, j + dj) for di, dj in directions if 0 <= i + di < n and 0 <= j + dj < n]

        bfs = deque([(0, 0)])  
        distance = 1

        while bfs:
            temp = deque()
            for (i, j) in bfs:
                if (i, j) == (n-1, n-1):  
                    return distance
                
                dist_dict[(i, j)] = distance
                for a, b in neighbour(i, j):
                    if grid[a][b] == 0 and (a, b) not in dist_dict:
                        temp.append((a, b))
                        dist_dict[(a, b)] = distance + 1 
                        grid[a][b] = 1  
                
            bfs = temp
            distance += 1
        
        return -1  



        ## Old code
        # n = len(grid)
        # if grid[n-1][n-1] !=0 or grid[0][0] != 0 : 
        #     return -1
        # dist_dict = dict()
        # def neighbour(i,j):
        #     delta_list = [(-1,-1), (-1,0), (-1, 1)
        #                  ,(0,-1),          (0, 1)
        #                  ,(1,-1),  (1,0),  (1, 1)]
        #     neigh = [(i+di, j+dj) for (di, dj) in delta_list if 0<=(i+di)<n and 0<=(j+dj)<n ]
        #     return neigh
        
        # bfs = [(n-1, n-1)]
        # distance = 1
        # while bfs: 
        #     temp = []
        #     for (i,j) in bfs:
        #         dist_dict[(i,j)] = distance
        #         grid[i][j] = 1
        #     for (i,j) in bfs:
        #         if (i,j) == (0,0):
        #             return distance
        #         neigh = neighbour(i,j)
        #         new_neigh = [(i,j) for (i,j) in neigh if (grid[i][j]== 0) ]
        #         # temp.extend(new_neigh)
        #         for a in new_neigh:
        #             temp.append(a)
        #     bfs = temp
        #     distance +=1
        # # print(dist_dict)
        # if (0,0) in dist_dict:
        #     return dist_dict[(0,0)]
        # else: 
        #     return -1
            

