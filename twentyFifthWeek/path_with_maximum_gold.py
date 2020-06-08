class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def backtrack(i, j, cur):
            backup = grid[i][j]
            grid[i][j] = 0
            max_gold = cur + backup
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] > 0:
                    max_gold = max(max_gold, backtrack(x, y, cur+backup))
            grid[i][j] = backup
            return max_gold

        m, n = len(grid), len(grid[0])
        return max(backtrack(i, j, 0) for i in range(m) for j in range(n))
