class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        n = len(nums)
        result = nums[n-2]
        i = 1
        j = n-4
        while i<j:
            result += nums[j]
            i +=1 
            j -=2
        return result
        

        
        