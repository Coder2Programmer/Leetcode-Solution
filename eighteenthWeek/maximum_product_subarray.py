class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = -0xFFFFFFFF
        cur_min = cur_max = 1
        for num in nums:
            if num < 0:
                cur_min, cur_max = cur_max, cur_min
            cur_min = min(num, num*cur_min)
            cur_max = max(num, num*cur_max)
            max_product = max(max_product, cur_max)
        return max_product