class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        n = len(nums)
        bucket = [[float('inf'), -float('inf')] for _ in range(n-1)]
        min_num, max_num = min(nums), max(nums)
        gap = math.ceil((max_num-min_num) / (n-1))
        for num in nums:
            if num == max_num:
                continue
            index = (num - min_num) // gap
            bucket[index][0] = min(bucket[index][0], num)
            bucket[index][1] = max(bucket[index][1], num)

        prev = min_num
        max_gap = 0
        for left, right in bucket:
            if left == float('inf'):
                continue
            max_gap = max(max_gap, left - prev)
            prev = right
        return max(max_gap, max_num - prev)
    