class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        right_limit, cur_index = 0, 0
        while cur_index <= right_limit and cur_index < len(nums):
            right_limit = max(right_limit, cur_index + nums[cur_index])
            cur_index += 1
        return cur_index >= len(nums)
        