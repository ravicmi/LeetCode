class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1 :
            return s
        dict_of_list = {i: '' for i in range(numRows)}
        direction = 1
        curr_pos = 0
        for index, letter in enumerate(s):
            dict_of_list[curr_pos] = dict_of_list[curr_pos] + letter
            curr_pos = curr_pos + direction
            if (curr_pos == 0) or (curr_pos == numRows-1) :
                direction = -direction
        final_str = ''
        for i in range(numRows):
            final_str += dict_of_list[i]
        return final_str
            

