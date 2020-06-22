class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        nums = [ord(c) - ord('a') for c in s]
        size = len(s) + 1
        dp = [0] * size
        for i in range(1, size):
            dp[i] = dp[i-1] ^ (1 << nums[i-1])
        ones = lambda x: bin(x).count('1')
        return [ones(dp[l] ^ dp[r+1]) >> 1 <= k for l, r, k in queries]
