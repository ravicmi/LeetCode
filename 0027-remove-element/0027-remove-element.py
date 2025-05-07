class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in nums: 
            if i== val:
                count +=1 
        for i in range(count):
            nums.remove(val)
        l = len(nums)
        return l
