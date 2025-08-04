class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        from functools import lru_cache
        possible_moves = [(i,j) for i in [-1,1] for j in [-2,2]] + [(i,j) for i in [-2,2] for j in [-1,1]]

        @lru_cache(None)
        def kp_dp(n, k, row, column):
            if (0 <= row <= (n-1)) and (0 <= column <= (n-1)):
                if k ==0:
                    return 1
                else: 
                    p = 0 
                    for (i,j) in possible_moves: 
                        p += 1/8 * (kp_dp(n, k-1, row+i, column+j))
                    return p
            else: 
                return 0 
        return kp_dp(n,k, row, column)