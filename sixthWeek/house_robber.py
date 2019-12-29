class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prev = 0
        cur = 0
        for num in nums:
            prev, cur = cur, max(cur, prev + num)

        return cur
