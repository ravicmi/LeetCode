class Solution:
    def maxProduct(self, n: int) -> int:
        l = [int(a) for a in str(n)]
        l.sort(reverse=True)
        a, b = l[:2]
        return a*b
        