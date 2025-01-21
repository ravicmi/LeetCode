class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1
        highest = max(height)
        max_area = (r-l)* min(height[l], height[r])
        while r>l:
            if height[l] < height[r]:
                l +=1
                area = (r-l)* min(height[l], height[r])
                max_area = max(max_area, area)
            else:
                r -=1
                area = (r-l)* min(height[l], height[r])
                max_area = max(max_area, area)
            if highest*(r-l) <= max_area:
                break

        
        return max_area