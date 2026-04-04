class Solution:
    from collections import defaultdict 
    def numIslands(self, grid: List[List[str]]) -> int:
        val = defaultdict(int)
        island = set()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island.add((i,j))
                    val[(i,j)] = 1

        no_of_islands = 0
        to_explore = set()
        def dir_list(cell):
            i, j  = cell
            return [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
        while island:
            cell = island.pop()
            to_explore.add(cell)
            while to_explore: 
                cell = to_explore.pop()
                island.discard(cell)
                val[cell] = 0
                for (i,j) in dir_list(cell):
                    if val[(i,j)] == 1:
                        to_explore.add((i,j))

            no_of_islands +=1 
        return no_of_islands
            

        