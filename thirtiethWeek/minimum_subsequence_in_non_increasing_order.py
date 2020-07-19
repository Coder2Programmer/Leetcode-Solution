class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        count = [0] * 107
        num_sum = sum(nums)
        for num in nums:
            count[num] += 1
        cur = 0
        subseq = []
        for i in range(100, 0, -1):
            while count[i]:
                count[i] -= 1
                subseq.append(i)
                cur += i
                if cur > num_sum - cur:
                    return subseq
        return subseq
    