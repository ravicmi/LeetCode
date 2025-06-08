class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n==1: 
            return True 
        res = self.canmakepos(nums, k)
        if res:
            return True
        nums = [-i for i in nums]
        res = self.canmakepos(nums, k)
        return res
        
        
    def canmakepos(self, nums:List[int], k: int) -> bool: 
        n = len(nums)
        l = 0 
        r = 0
        flip_count = 0 
        while r<n and flip_count<=k:
            while l<n :
                if nums[l]==-1:
                    break
                l+=1
            r = l+1
            while r<n :
                if nums[r]==-1:
                    break
                r+=1
            if r<n: 
                flip_count += r-l
                l = r+1
                r = r+1
        print('check_point = 1',l,r, flip_count)
        if flip_count>k:
            return False
        
        if l > n-1:
            return True
        else:
            return False
                
            
            

            
        
        
        