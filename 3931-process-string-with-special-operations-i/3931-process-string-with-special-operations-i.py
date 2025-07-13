class Solution:
    def processStr(self, s: str) -> str:
        res = ''
        for a in s: 
            if a == '*':
                res = res[:-1]
            elif a == '#':
                res = res+res
            elif a == '%':
                res = res[::-1]
            else: 
                res += a
        return res
            
        