class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (1+len2) for _ in range(1+len1)]
        for i in range(len1):
            for j in range(len2):
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j]+(word1[i]==word2[j]))
                
        return len1 + len2 - 2 * dp[-1][-1]