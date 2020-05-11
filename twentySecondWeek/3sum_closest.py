class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = sum(nums[:3])
        for left in range(len(nums)-2):
            mid, right = left+1, len(nums)-1
            while mid < right:
                cur_sum = nums[left] + nums[mid] + nums[right]
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum
                if cur_sum < target:
                    mid += 1
                else:
                    right -= 1
        return closest_sum
