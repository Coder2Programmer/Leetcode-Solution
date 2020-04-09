class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices)//2:
            return sum(max(0, prices[i+1]-prices[i]) for i in range(len(prices)-1))
        dp = [[-0xFFFFFFFF, 0] for _ in range(k+1)]
        for price in prices:
            for i in range(1, k+1):
                dp[i][1] = max(dp[i][1], dp[i][0]+price)
                dp[i][0] = max(dp[i][0], dp[i-1][1]-price)
        return dp[-1][-1]