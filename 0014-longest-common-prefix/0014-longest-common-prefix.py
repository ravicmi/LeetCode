class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = 200
        out = ''
        for s in strs: 
            minLen = min(minLen, len(s))
        is_common = True
        i = 0
        while (i < minLen) & (is_common):
            l = strs[0][i]
            for s in strs: 
                if s[i] != l:
                    is_common = False
            if is_common:
                out += l
            i +=1 
        return out


