class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0 
        high = len(nums)-1
        if high ==-1:
            return [-1, -1]
        def bs_lower(nums, i, j):
            if i+1>=j:
                if nums[i] == target:
                    return i
                elif nums[j] == target:
                    return j 
                else:
                    return -1
            else:
                mid = (i+j)//2
                if nums[mid] >=target:
                    return bs_lower(nums, i, mid)
                else: 
                    return bs_lower(nums, mid, j)
            
        def bs_upper(nums, i, j):
            # print(i,j)
            if i+1>=j:
                if nums[j] == target:
                    return j
                elif nums[i] == target:
                    return i 
                else:
                    return -1
            else:
                mid = (i+j)//2
                if nums[mid] > target:
                    return bs_upper(nums, i, mid)
                else: 
                    return bs_upper(nums, mid, j)

        a = bs_lower(nums, low, high)
        b = bs_upper(nums, low, high)
        return [a,b]


        