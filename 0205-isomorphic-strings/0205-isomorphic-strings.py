class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pair_set = set()
        left_set = set()
        right_set = set()
        n = len(s)
        for i in range(n):
            pair_set.add((s[i], t[i]))
            left_set.add(s[i])
            right_set.add(t[i])
        if len(pair_set) != len(left_set):
            return False
        if len(pair_set) != len(right_set):
            return False
        return True

        