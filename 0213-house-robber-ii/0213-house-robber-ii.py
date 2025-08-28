class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import lru_cache
        n = len(nums)

        @lru_cache(None)
        def dp(i, last): 
            if i ==n-1:
                if last:
                    return  nums[i]
                else:
                    return 0
            if i == n-2: 
                if last: 
                    return max(nums[i], nums[i+1])
                else: 
                    return nums[i]
            if i ==0:
                return max(nums[0]+dp(2, False), dp(1, True)) 
            
            return max(nums[i]+dp(i+2, last), dp(i+1, last))
        
        return dp(0, True)
            


        