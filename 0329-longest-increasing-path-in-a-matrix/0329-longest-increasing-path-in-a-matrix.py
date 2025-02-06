from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        
        # Memoization for DP
        @lru_cache(None)
        def dfs(i, j):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up
            max_path = 1
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    max_path = max(max_path, 1 + dfs(ni, nj))
            return max_path

        return max(dfs(i, j) for i in range(m) for j in range(n))