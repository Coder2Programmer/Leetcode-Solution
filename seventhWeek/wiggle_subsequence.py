class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                up = down + 1
            elif nums[i-1] > nums[i]:
                down = up + 1

        return max(up, down)
