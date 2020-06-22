class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        dp = [[False] * (1+p_len) for _ in range(1+s_len)]
        dp[0][0] = True
        for i in range(1+s_len):
            for j in range(1, 1+p_len):
                if p[j-1] != '*':
                    dp[i][j] = i and dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='.')
                else:
                    dp[i][j] = dp[i][j-2] or (i and dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                    
        return dp[-1][-1]
    