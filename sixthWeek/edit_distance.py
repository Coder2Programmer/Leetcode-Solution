class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[max(i, j) for j in range(1 + len(word2))] 
              for i in range(1 + len(word1))]

        for i in range(1, 1 + len(word1)):
            for j in range(1, 1 + len(word2)):
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], 
                                   dp[i-1][j-1] - int(word1[i-1] == word2[j-1]))

        return dp[-1][-1]
