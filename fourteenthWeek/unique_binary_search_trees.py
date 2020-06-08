class Solution:
    def numTrees(self, n: int) -> int:
        def helper(n: int) -> int:
            nonlocal memo
            if memo[n]:
                return memo[n]
            memo[n] = sum(helper(i)*helper(n-1-i) for i in range(n))
            return memo[n]
        
        memo = collections.Counter([0, 1])
        return helper(n)
    

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(2, n+1):
            dp[i] = sum(dp[j]*dp[i-1-j] for j in range(i))
            
        return dp[-1]


