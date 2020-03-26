class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        board_filter = lambda p: 0 <= p[0] < m and 0 <= p[1] < n and board[p[0]][p[1]] == 'O'
        queue = list(filter(board_filter, [(x, y) for r in range(max(m, n)) 
                                           for x, y in ((r, 0), (r, n-1), (0, r), (m-1, r))]))
        while queue:
            x, y = queue.pop()
            board[x][y] = 'W'
            queue.extend(list(filter(board_filter, ((x-1, y), (x+1, y), (x, y-1), (x, y+1)))))
        for row in board:
            for i, c in enumerate(row):
                row[i] = 'XO'[c=='W']