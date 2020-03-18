class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(x: int, y: int, index: int) -> bool:
            if index >= len(word):
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]) or board[x][y] != word[index]:
                return False
            board[x][y] = None
            exist = any(helper(x+dx, y+dy, index+1) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)))
            board[x][y] = word[index]
            return exist
        
        return any(helper(x, y, 0) for x in range(len(board)) for y in range(len(board[x])))    
        