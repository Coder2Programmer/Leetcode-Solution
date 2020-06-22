class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_num = 0
        for i in range(31, -1, -1):
            max_num <<= 1
            prefixes = {num >> i for num in nums}
            max_num |= any(max_num + 1 ^ prefix in prefixes for prefix in prefixes)
        return max_num
    