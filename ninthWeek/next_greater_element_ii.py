class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nums_len = len(nums)
        next_num = [-1] * nums_len
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                next_num[stack.pop()] = num
            stack.append(i)
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                next_num[stack.pop()] = num
            if not stack:
                break
        return next_num
        