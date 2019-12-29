class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_string = ''
        if not s:
            return longest_string

        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i+1][j-1]);
                longest_string = s[i:j+1] if dp[i][j] and j - i + 1 > len(longest_string) else longest_string

        return longest_string
