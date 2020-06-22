class Solution:
    def solverNQueens(self, n: int) -> List[List[str]]:
        def backtrack(r):
            if r == n:
                result.append([''.join(row) for row in board])
                return
            for c in range(n):
                if is_valid(r, c):
                    board[r][c] = 'Q'
                    backtrack(r+1)
                    board[r][c] = '.'

        def is_valid(r, c):
            for i in range(n):
                for j in range(n):
                    if board[i][j] = 'Q' and (c == j or i+j == r+c or i-j == r-c):
                        return False
            return True
            
        board = [['.'] * n for _ in range(n)]
        result = []
        backtrack(0)
        return result