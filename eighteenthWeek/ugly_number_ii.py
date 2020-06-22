class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        index_2 = index_3 = index_5 = 0
        for _ in range(n-1):
            num_2, num_3, num_5 = dp[index_2]*2, dp[index_3]*3, dp[index_5]*5
            min_num = min(num_2, num_3, num_5)
            dp.append(min_num)
            index_2 += int(min_num == num_2)
            index_3 += int(min_num == num_3)
            index_5 += int(min_num == num_5)
        return dp[-1]