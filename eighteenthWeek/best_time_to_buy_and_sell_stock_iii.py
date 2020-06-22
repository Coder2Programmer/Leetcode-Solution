class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_hold = second_hold = -0xFFFFFFFF
        first_release = second_release = 0
        for price in prices:
            second_release = max(second_release, second_hold+price)
            second_hold = max(second_hold, first_release-price)
            first_release = max(first_release, first_hold+price)
            first_hold = max(first_hold, -price)            
        return second_release