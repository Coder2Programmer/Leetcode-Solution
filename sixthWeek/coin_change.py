class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1

        dp = [amount + 1] * (1 + amount)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin] + 1)

        return -1 if dp[-1] > amount else dp[-1]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1

        dp = [amount + 1] * (1 + amount)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return -1 if dp[-1] > amount else dp[-1]
