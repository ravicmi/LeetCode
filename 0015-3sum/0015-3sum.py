class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict
        d= defaultdict(int)
        for i in nums:
            d[i] +=1
        s = sorted(d.keys())
        l = 0
        length = len(s)
        result = []
        for l in range(length):
            for r in range(length-1, l, -1):
                mid = -(s[l] + s[r])
                if (s[l]<mid) and (s[r]>mid) and d[mid]>0:
                    result.append([mid, s[l], s[r]])
                if (s[l]==mid) and (s[r]>mid) and d[mid]>1:
                    result.append([mid, s[l], s[r]])
                if (s[l]<mid) and (s[r]==mid) and d[mid]>1:
                    result.append([mid, s[l], s[r]])
                if (s[l]==mid) and (s[r]==mid) and d[mid]>2:
                    result.append([mid, s[l], s[r]])
        if d[0]>2:
            result.append([0,0,0])

        return result 



