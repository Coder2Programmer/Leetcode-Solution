class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = cur = 0
        for num in nums:
            if count == 0:
                cur = num
            count += (cur == num) or -1
        return cur
