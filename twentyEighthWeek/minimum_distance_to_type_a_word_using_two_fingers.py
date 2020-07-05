class Solution:
    def minimumDistance(self, word: str) -> int:
        def dis(a, b):
            return a and abs(a//6 - b//6) + abs(a%6 - b%6)
        
        dp, dp2 = {(0, 0): 0}, {}
        for c in (ord(c)+1 for c in word):
            for a, b in dp:
                dp2[c, b] = min(dp2.get((c, b), 3000), dp[a, b] + dis(a, c))
                dp2[a, c] = min(dp2.get((a, c), 3000), dp[a, b] + dis(b, c))
        return min(dp.values())
