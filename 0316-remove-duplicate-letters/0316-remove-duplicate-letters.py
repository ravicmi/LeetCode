class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        last_index = dict()
        stack = []
        for index, i in enumerate(s):
            last_index[i] = index
        for index, i in enumerate(s): 
            if i in seen: 
                continue
            while stack and stack[-1] > i and last_index[stack[-1]]> index: 
                seen.remove(stack.pop()) 
            stack.append(i)
            seen.add(i)
            print(index, i, stack)
        out = ''.join(stack)
        return out



