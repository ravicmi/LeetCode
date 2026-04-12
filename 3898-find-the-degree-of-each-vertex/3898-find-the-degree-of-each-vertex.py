class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        out = []
        n = len(matrix)
        for i in range(n):
            out.append(sum(matrix[i]))
        return out
        