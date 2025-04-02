class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        j = 0 
        for k in range(len(nums)-1):
            i += 1
            if nums[i] != nums[i-1]:
                j += 1
                nums[j] = nums[i]
        return j+1


        