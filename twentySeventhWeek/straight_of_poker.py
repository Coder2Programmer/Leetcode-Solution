class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        joker = 0
        for i in range(4):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i+1]:
                return False
        return nums[4] - nums[joker] < 5
        