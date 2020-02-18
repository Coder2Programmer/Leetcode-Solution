class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, cur = 0, 0
        for num in nums:
            if not count:
                cur = num
            count += 1 if num == cur else -1
        return cur