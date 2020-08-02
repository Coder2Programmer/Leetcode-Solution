class Solution:
    def allPossibleFBT(N: int) -> List[TreeNode]:
        def helper(n):
            if n in memo:
                return memo[n]
            for i in range(1, n, 2):
                for left in helper(i):
                    for right in helper(n-1-i):
                        memo[n].append(TreeNode(0, left, right))
            return memo[n]
        memo = collections.defaultdict(list, {1: [TreeNode(0)]})
        return helper(N)