class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)

        for right in range(len(nums)):
            for left in range(right):
                if nums[left] < nums[right]:
                    dp[right] = max(dp[right], dp[left] + 1)

        return max(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = []
        for num in nums:
            index = bisect.bisect_left(dp, num)
            if index < len(dp):
                dp[index] = num
            else:
                dp.append(num)

        return len(dp)
