class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 1:
            return -1

        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        rotated_len = low
        low, high = 0, len(nums)
        while low < high:
            mid = low + (high - low) // 2
            true_mid = (mid + rotated_len) % len(nums)
            if nums[true_mid] < target:
                low = mid + 1
            else:
                high = mid
        index = (low + rotated_len) % len(nums)
        return index if nums[index] == target else -1
