class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums: List[int]) -> int:
            prev = cur = 0
            for num in nums:
                prev, cur = cur, max(cur, prev+num)
            return cur
        return max(helper(nums[:-1]), helper(nums[len(nums)!=1:]))