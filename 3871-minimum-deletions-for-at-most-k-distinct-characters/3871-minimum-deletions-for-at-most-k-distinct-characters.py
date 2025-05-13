class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        from collections import defaultdict
        dict = defaultdict(int)
        for a in s: 
            dict[a] +=1
        values = sorted(list(dict.values()), reverse = True)
        out = 0 
        for i in values[k:]:
            out +=i
        return out
        
        
        