class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        prev_num = None
        prev = cur = 0
        for k, v in sorted(counter.items()):
            if prev_num != k - 1:
                prev, cur = cur, cur + k * v
            else:
                prev, cur = cur, max(cur, prev + k*v)
            prev_num = k
        return cur
