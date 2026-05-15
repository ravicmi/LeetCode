class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin = min(coins)

        from functools import lru_cache 

        @lru_cache(maxsize=None)
        def min_way(amount):
            if amount ==0: 
                return 0
            if amount < min_coin:
                return float('inf')
            curr_min = float('inf')
            for coin in coins: 
                curr_min = min(curr_min, 1+min_way(amount-coin))

            return curr_min
        final_min = min_way(amount)
        return -1 if final_min > 1e5 else final_min

            
        

