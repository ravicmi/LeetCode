class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        bracket_stack = []
        index_stack = []
        remove_index = []
        for index, char in enumerate(s):
            if char == '(':
                bracket_stack.append(char)
                index_stack.append(index)
            if char == ')':
                if bracket_stack and bracket_stack[-1] == '(':
                    bracket_stack.pop()
                    index_stack.pop()
                else : 
                    remove_index.append(index)
        remove_index = remove_index + index_stack
        s_list = [a for a in s]
        for i in remove_index[::-1]:
            s_list.pop(i)
        s_final = ''.join(s_list)
        return s_final
