class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = cur_profit = 0
        for i in range(len(prices)-1):
            cur_profit = max(0, cur_profit+prices[i+1]-prices[i])
            max_profit = max(max_profit, cur_profit)
        return max_profit