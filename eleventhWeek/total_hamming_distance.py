class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        shift_count = math.ceil(math.log(max(nums), 2)) + 1
        distance, n = 0, len(nums)
        for _ in range(shift_count):
            ones = sum(num & 1 for num in nums)
            distance += ones * (n - ones)
            for i in range(n):
                nums[i] >>= 1
        return distance