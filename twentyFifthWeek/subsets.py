class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        state = 2**len(nums)
        sets = [[] for _ in range(state)]
        for i in range(state):
            for j in range(len(nums)):
                if (i >> j) & 1:
                    sets[i].append(nums[j])
        return sets
