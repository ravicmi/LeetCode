class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_set = {i: set() for i in range(9)}
        col_set = {i: set() for i in range(9)}
        block_set = {(i,j): set() for i in range(3) for j in range(3)}
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value != ".":
                    row_set[i].add(value)
                    col_set[j].add(value)
                    block_set[(i//3, j//3)].add(value)
        
        tran = [(i,j) for i in range(9) for j in range(9)]

        def back_track(t,board):
            if t==81:
                return True
            i,j = tran[t]
            if board[i][j] != ".":
                return back_track(t+1, board)
            for value in map(str, range(1,10)):
                if (value in row_set[i]) or (value in col_set[j]) or (value in block_set[(i//3, j//3)]):
                    continue
                else: 
                    row_set[i].add(value)
                    col_set[j].add(value)
                    block_set[(i//3, j//3)].add(value)
                    board[i][j] = str(value)
                    if back_track(t+1, board):
                        return True
                    row_set[i].remove(value)
                    col_set[j].remove(value)
                    block_set[(i//3, j//3)].remove(value)
                    board[i][j] = "."
            # return False

        back_track(0, board)





