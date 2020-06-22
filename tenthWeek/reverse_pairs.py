class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        nums_len = len(nums)
        nums_copy = sorted(nums)
        bit = [0] * (nums_len + 1)
        reverse_pair_count = 0
        for i in range(nums_len):
            reverse_pair_count += self.query(bit, bisect.bisect_left(nums_copy, 2*nums[i]+1)+1)
            self.update(bit, bisect.bisect_left(nums_copy, nums[i])+1, 1)
        return reverse_pair_count
    
    def update(self, bit: list, index: int, value: int) -> None:
        while index > 0:
            bit[index] += value
            index -= index & (-index)
            
    def query(self, bit: list, index: int) -> int:
        ret = 0
        while index < len(bit):
            ret += bit[index]
            index += index & (-index)
        return ret
