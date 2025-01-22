class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for index, height in enumerate(heights):
            if len(stack) ==0:
                stack.append((index, height))
            elif stack[-1][1] <= height:
                stack.append((index, height))
            else: 
                while stack[-1][1] > height:
                    last_index, last_height = stack.pop()
                    max_area = max(max_area, (index-last_index)*last_height)
                    if len(stack)==0:
                        break
                stack.append((last_index, height))
        # if len(stack) > 0 : 
        #     (index_end, height_end)  = stack.pop()
        #     max_area = max(max_area, height_end)
        for (index, height) in stack:
            max_area = max(max_area, height*(len(heights)-index))

        return max_area

                

        