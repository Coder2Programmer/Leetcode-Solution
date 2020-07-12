class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        right = -float('inf')
        for num in nums:
            if num < right:
                return True
            while stack and stack[-1] < num:
                right = stack.pop()
            stack.append(num)
        return False
    