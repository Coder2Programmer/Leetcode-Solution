class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for start in num_set:
            if start-1 not in num_set:
                end = start + 1
                while end in num_set:
                    end += 1
                max_len = max(max_len, end-start)
        return max_len
