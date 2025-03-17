class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        # ccs = dict()
        ccs_inv = dict()
        ccs_size = dict()
        n = len(grid)
        viewed_cell = set()
        delta = [(-1,0), (1,0), (0,-1), (0, 1)]
        def cc_start(i,j, name): 
            viewed_cell.add((i,j))
            curr_block = [(i,j)]
            ccs_inv[(i,j)] = name 
            dq = deque()
            dq.append((i,j))
            
            def bfs(dq):
                nonlocal viewed_cell
                nonlocal curr_block
                nonlocal ccs_inv
                if not dq:
                    return 
                i,j = dq.popleft()
                neigh = [(i+di, j+dj) for di,dj in delta if 0<=i+di <= n-1 and 0<=j+dj <= n-1 and grid[i+di][j+dj]==1 and (i+di,j+dj) not in viewed_cell]
                curr_block.extend(neigh)
                for i,j in neigh : 
                    viewed_cell.add((i,j))
                    ccs_inv[(i,j)] = name
                dq.extend(neigh)
                bfs(dq)
                return 
            bfs(dq)
            # print(name )
            # print(curr_block)
            return curr_block

        name = 1
        max_island = 0
        for i in range(n):
            for j in range(n):
                if (i,j) not in viewed_cell and grid[i][j] == 1: 
                    curr_block = cc_start(i,j, name)
                    # ccs[name] = curr_block
                    ccs_size[name] = len(curr_block)
                    max_island = max(max_island, len(curr_block) )
                    name +=1 
        
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0 :
                    neigh = [(i+di, j+dj) for di, dj in delta if 0<=i+di <= n-1 and 0<=j+dj <= n-1 and grid[i+di][j+dj]==1 ]
                    block_list = {ccs_inv[(i,j)] for i,j in neigh}
                    # print(i,j)
                    # print(neigh)
                    # print(block_list)
                    max_local = sum([ccs_size[name] for name in block_list])
                    max_island = max(max_island, max_local)
        total_sum = sum([sum(a) for a in grid])
        return max_island + 1 if total_sum < n*n else max_island


            








