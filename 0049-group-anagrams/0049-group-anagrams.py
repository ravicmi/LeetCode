class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        out = defaultdict(list)
        for st in strs: 
            str_sort = ''.join(sorted(st))
            out[str_sort].append(st)
        res = [a for a in out.values()]
        return res
        