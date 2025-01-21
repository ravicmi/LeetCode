class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        explored_index = 0
        numsize = len(nums)
        inf = max(nums)+2
        
        while explored_index <= numsize-1 :
            curr_index = explored_index
            curr_value = nums[curr_index]
            while curr_value>=1 and curr_value<=len(nums) and curr_value != inf:
                curr_index = curr_value-1
                curr_value = nums[curr_index]
                nums[curr_index] = inf
            
            explored_index +=1
        required_index = 1
        for i in nums:
            if i==inf:
                required_index +=1
            else:
                break
        return required_index



        