class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix_sum[j+1] - self.prefix_sum[i]
        