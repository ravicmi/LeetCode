class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        oppo = {'(':')', '{':'}', '[':']'}
        start_brac = {'(', '{', '['}
        for i in s: 
            if i in start_brac:
                stack.append(oppo[i])
            elif len(stack)==0:
                return False
            else: 
                last = stack.pop()
                if i != last:
                    return False
        if stack:
            return False
        else:
            return True