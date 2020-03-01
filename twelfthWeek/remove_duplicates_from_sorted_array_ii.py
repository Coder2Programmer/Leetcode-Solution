class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        
        index = 2
        for num in nums[2:]:
            if num > nums[index-2]:
                nums[index] = num
                index += 1
        return index
    