class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        delta = [(-1,0), (1,0), (0,1), (0,-1)]
        max_dict = dict()
        m = len(matrix)
        n = len(matrix[0])
        # global global_max
        global_max = 0 
        def max_path(i,j):
            nonlocal global_max
            if (i,j) in max_dict:
                return max_dict[(i,j)]
            neigh = [(i+di, j+dj) for di,dj in delta if 0<= i+di<= m-1 and 0<=j+dj<=n-1 and matrix[i+di][j+dj]>matrix[i][j]]
            max_local = 0 
            for ni,nj in neigh:
                n_path_len = max_path(ni, nj)
                if n_path_len>max_local:
                    max_local = n_path_len
            max_local += 1
            max_dict[(i,j)] = max_local
            if max_local > global_max:
                global_max = max_local
            return max_local
        

        for i in range(m):
            for j in range(n):
                if (i,j) not in max_dict:
                    max_path(i,j)
        return global_max