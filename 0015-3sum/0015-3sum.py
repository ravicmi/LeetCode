class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        n = len(nums)
        i = 0 
        while i<= n-2:
            if nums[i]>0:
                break
            j = i+1
            k = n-1
            while j<k:
                sum3 = nums[i]+nums[j]+nums[k]
                if sum3==0:
                    out.append([nums[i], nums[j], nums[k]])
                    while k>j and nums[k]==nums[k-1] :
                        k -=1
                    while  k>j and nums[j]==nums[j+1] :
                        j+=1
                    k-=1
                    j+=1
                elif sum3 > 0:
                    while k>j and nums[k]==nums[k-1] :
                        k -=1
                    k -=1
                else: 
                    while k>j and nums[j]==nums[j+1]:
                        j+=1
                    j+=1
            while i<=n-2 and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return out









        # from collections import defaultdict
        # dict = defaultdict(list)
        # for index, i in enumerate(nums): 
        #     dict[i].append(index)
        # n = len(nums)
        # out = set()
        # for i in range(n):
        #     for j in range(i+1, n):
        #         ni = nums[i]
        #         nj = nums[j]
        #         nk = -ni-nj
        #         for k in dict[nk]:
        #             if k>j:
        #                 a,b,c = sorted([ni, nj,nk])
        #                 out.add((a,b,c))
        # out = list(out)
        # return out