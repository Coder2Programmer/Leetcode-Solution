class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        rest = 0
        buy = -0xFFFFFFFF
        sell = 0
        for price in prices:
            prev_sell = sell
            sell = buy + price
            buy = max(buy, rest - price)
            rest = max(rest, prev_sell)

        return max(rest, sell)

