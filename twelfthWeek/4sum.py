class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        two_sum_dict = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                two_sum_dict[nums[i]+nums[j]].append((i,j))
                
        four_sum_set = set()
        for two_sum in two_sum_dict:
            need_sum = target - two_sum
            if need_sum not in two_sum_dict:
                continue
            for (i, j) in two_sum_dict[two_sum]:
                for (k, l) in two_sum_dict[need_sum]:
                    if k != i != l and k != j != l:
                        four_sum_set.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
        
        return list(four_sum_set)