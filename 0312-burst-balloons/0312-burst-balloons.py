class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        from functools import lru_cache
        nums = [1] + nums +[1]
        n = len(nums)
        @lru_cache(None)
        def dp(i, j):
            if j <= i+1:
                return 0
            a = 0 
            for mid in range(i+1, j):
                loc = nums[i]*nums[mid]*nums[j] + dp(i, mid) + dp(mid, j)
                a = max(loc, a)
            return a
        return dp(0, n-1)


