class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir = [(-1,0), (1,0), (0,1), (0,-1)]
        rot = []
        good = 0
        level = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: 
                    rot.append((i,j))
                if grid[i][j] == 1 : 
                    good +=1
        while rot: 
            next_rot = []
            for rl, rr in rot: 
                for nl, nr in dir: 
                    l,r = rl+nl, rr+nr
                    if l>=0 and l< m and r >=0 and r < n and grid[l][r] == 1:
                        grid[l][r] = 2
                        good -= 1
                        next_rot.append((l,r))
            if next_rot:
                level +=1 
            rot = next_rot

        return -1 if good else level
        

                    


        