class Solution:
    def trap(self, height: List[int]) -> int:
        left_list = []
        right_list = []
        my_max = 0
        for i in height:
            left_list.append(my_max)
            my_max = max(my_max,i)

        my_max = 0
        for i in height[::-1]:
            right_list.append(my_max)
            my_max = max(my_max,i)
        right_list = right_list[::-1]
        water_trap = 0 
        for i in range(len(height)):
            curr_trap = max(min(left_list[i], right_list[i])-height[i], 0)
            water_trap += curr_trap
        return water_trap
        
        