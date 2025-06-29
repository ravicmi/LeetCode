class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        curr = ''
        n = len(s)
        i = 0 
        out = []
        while i<n: 
            curr += s[i]
            if curr not in seen: 
                seen.add(curr)
                out.append(curr)
                curr = ''
            i +=1
        return out
                
        