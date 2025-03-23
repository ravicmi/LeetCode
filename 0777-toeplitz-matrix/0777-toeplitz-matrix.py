class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        col = 0 
        while col < n-1:
            curr = matrix[0][col]
            incr = 1
            while col+incr < n and incr < m : 
                if curr != matrix[incr][col+incr]:
                    return False
                incr +=1 
            col +=1 
        
        row = 0 
        while row < m-1:
            curr = matrix[row][0]
            incr = 1
            while row+incr < m and incr < n : 
                if curr != matrix[row+incr][incr]:
                    return False
                incr +=1 
            row += 1 
        return True
        








        # for i in range(m):
        #     curr = matrix[i][0]
        #     for j in range(1,min(n, m-i)):
        #         if curr != matrix[i+j][i]:
        #             return False
            
        # for j in range(1, n):
        #     curr = matrix[0][j]
        #     for i in range(1, min(m, n-j)):
        #         if curr != matrix[i][i+j]:
        #             return False

        # return True