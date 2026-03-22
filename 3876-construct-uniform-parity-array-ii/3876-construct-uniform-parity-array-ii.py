class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min1 = min(nums1)
        has_odd = False
        for i in nums1:
            if i%2==1:
                has_odd = True
        if min1%2:
            return True
        if not has_odd:
            return True
        return False



        
        # max1 = max(nums1)
        # min1 = min(nums1)
        # out = False
        # has_odd = False
        # for i in nums1:
        #     if i%2==1:
        #         has_odd = True
        # if max1%2==1:
        #     if min1%2==1:
        #         out = True
            
        # if max1%2==0:
        #     if not (has_odd): 
        #         out = True
        # return out
        
        