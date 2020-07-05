class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            for dis, length in list(dp.items()):
                dp[dis+rod] = max(dp.get(dis+rod, 0), length)
                dp[abs(dis-rod)] = max(dp.get(abs(dis-rod), 0), length+min(dis, rod))
        return dp[0]
