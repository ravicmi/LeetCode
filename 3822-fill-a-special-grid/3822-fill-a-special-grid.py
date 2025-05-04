class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        mat = [[-1 for i in range(2**N)] for j in range(2**N)]
        def specialSubGrid(i, j, start_num, size):
            # print(i, j, start_num, size)
            if size == 1:
                mat[i][j] = start_num
                return
            new_size = size//2
            specialSubGrid(i,j, start_num, new_size)
            new_start_num = start_num + new_size*new_size
            new_i, new_j = i+new_size, j
            specialSubGrid(new_i, new_j, new_start_num, new_size)
            new_start_num = new_start_num + new_size*new_size
            new_i, new_j = i+new_size, j-new_size
            specialSubGrid(new_i, new_j, new_start_num, new_size)
            new_start_num = new_start_num + new_size*new_size
            new_i, new_j = i, j-new_size
            specialSubGrid(new_i, new_j, new_start_num, new_size)
            return
        specialSubGrid(0, 2**N-1, 0, 2**N)
        return mat