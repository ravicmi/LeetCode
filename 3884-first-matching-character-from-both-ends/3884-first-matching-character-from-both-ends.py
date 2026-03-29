class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        out = -1
        for i in range((n+1)//2):
            if s[i]==s[-(i+1)]:
                out = i
                break
        return out
        
            
        
        