class Solution:
    def findMin(self, nums: List[ing]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) >> 1
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
    