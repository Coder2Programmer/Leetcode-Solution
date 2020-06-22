class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [nums[:]]
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i-1]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        nums[i:] = nums[len(nums)-1:i-1:-1]
                        res.append(nums[:])
                        break
                i = len(nums) - 1
            else:
                i -= 1
        return res