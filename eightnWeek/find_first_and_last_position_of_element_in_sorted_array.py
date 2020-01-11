class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.find_first(nums, target),
                self.find_last(nums, target)]
        
    def find_first(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        
        return low if low < len(nums) and nums[low] == target else -1
    
    def find_last(self, nums: List[int], target: int) -> int:
        low, high = -1, len(nums) - 1
        while low < high:
            mid = high - (high - low) // 2
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid
        
        return low if low > -1 and nums[low] == target else -1