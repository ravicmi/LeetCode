class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        n = len(nums)/2
        print(n)
        print(count)
        for i, c in count.items():
            if c>n: 
                return i


        