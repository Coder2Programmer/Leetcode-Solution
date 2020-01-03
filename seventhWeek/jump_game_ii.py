class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) <= 1:
            return 0
        
        left, right = 0, nums[0]
        jump_number = 1
        while right < len(nums) - 1:
            left, right = right, max(i + nums[i] for i in range(left, right + 1))
            jump_number += 1

        return jump_number


class Solution:
    def jump(self, nums: List[int]) -> int:
        end, next_end = 0, 0
        jump_number = 0
        for i in range(len(nums) - 1):
            next_end = max(next_end, i + nums[i])
            if i >= end:
                jump_number += 1
                end = next_end

        return jump_number
