class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0 
        if x <3 :
            return 1
        u = x
        l = 1
        while u > l+1:
            mid = (u+l)//2
            if mid*mid <= x:
                l = mid
            else: 
                u = mid
        return l
        

