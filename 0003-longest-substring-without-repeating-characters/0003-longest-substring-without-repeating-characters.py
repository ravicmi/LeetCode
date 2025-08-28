class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        d = deque()
        l = 0
        seen = set()
        for i in s: 
            if i not in seen:
                seen.add(i)
                d.append(i)
                l = max(l, len(seen))
            else: 
                while i != d[0]:
                    seen.remove(d.popleft())
                d.popleft()
                d.append(i)
        return l

        
        

        