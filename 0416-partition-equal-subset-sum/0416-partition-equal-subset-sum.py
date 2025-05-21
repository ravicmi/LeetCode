class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total/2
        if total%2 :
            return False
        dp = set([0])
        for num in nums:
            next_dp = dp.copy()
            for t in dp:
                if t+num == target:
                    return True
                next_dp.add(t+num)
            dp = next_dp
        return False
