class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for index, i in enumerate(nums):
            d[i] = index
        for i in range(len(nums)):
            conj = target-nums[i]
            if conj in d and i!= d[conj]:
                return [i, d[conj]] 

        