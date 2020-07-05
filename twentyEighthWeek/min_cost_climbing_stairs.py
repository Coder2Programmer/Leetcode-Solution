class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = cur = 0
        for c in cost:
            prev, cur = cur, c + min(prev, cur)
        return min(prev, cur)
