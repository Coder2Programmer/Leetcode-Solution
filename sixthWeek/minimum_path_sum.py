class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        dp = grid.copy()
        for i in range(1, len(dp)):
            dp[i][0] += dp[i-1][0]
        for j in range(1, len(dp[0])):
            dp[0][j] += dp[0][j-1]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
     