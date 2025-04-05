class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        from collections import defaultdict
        wordDict = defaultdict(int)
        for l in s:
            wordDict[l] +=1 
        keys = wordDict.keys()
        keys = sorted(keys, reverse = True)
        i = 0
        j = 1
        n = len(keys)
        res = ''
        while  j<n: 
            ikey = keys[i]
            jkey = keys[j]
            if wordDict[jkey]==0: 
                j +=1 
            elif wordDict[ikey] <= repeatLimit:
                res += ikey*(wordDict[ikey])
                i = j 
                j +=1
                wordDict[ikey] = 0
            else: 
                res += ikey*repeatLimit
                res += jkey
                wordDict[jkey] -=1
                wordDict[ikey] -=repeatLimit
        ikey = keys[i]
        res += ikey*(min(wordDict[ikey], repeatLimit))
        return res



