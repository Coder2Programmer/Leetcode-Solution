class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell, buy = 0, -0xFFFFFFFF
        for price in prices:
            prev_buy = buy
            buy = max(buy, sell - price)
            sell = max(sell, prev_buy + price - fee)

        return sell
