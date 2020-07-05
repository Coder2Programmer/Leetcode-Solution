class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        
        pre_sum = [0]
        for i, num in enumerate(nums):
            elem = (pre_sum[-1] + num) % k if k else pre_sum[-1] + num
            pre_sum.append(elem)
        
        seen = set()
        for i in range(len(pre_sum)-2):
            seen.add(pre_sum[i])
            if pre_sum[i+2] in seen:
                return True
        return False
    