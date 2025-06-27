class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        upc_dict = dict()        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        upc_dict[(m-1, n-1)] = 1-obstacleGrid[m-1][n-1]
        for j in range(n-2, -1, -1):
            if obstacleGrid[m-1][j]==0:
                upc_dict[(m-1,j)] = upc_dict[(m-1,j+1)]
            else: 
                upc_dict[(m-1,j)] = 0
        # print(upc_dict)
        for i in range(m-2, -1, -1):
            if obstacleGrid[i][n-1]==0:
                upc_dict[(i, n-1)] = upc_dict[(i+1,n-1)]
            else: 
                upc_dict[(i, n-1)] = 0
        if n==1 or m==1: 
            return upc_dict[(0,0)]
        for j in range(n-2, -1, -1):
            for i in range(m-2, -1, -1):
                if obstacleGrid[i][j] == 0: 
                    upc_dict[(i, j)] = upc_dict[(i+1, j)] + upc_dict[(i, j+1)]
                else: 
                    upc_dict[(i, j)] = 0
        print(upc_dict)
        return upc_dict[(0,0)]


        