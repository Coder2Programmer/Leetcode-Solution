class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums, pos, result = sorted(nums), {}, [[]]
        for num in nums:
            start, cur_len = pos.get(num, 0), len(result)
            result.extend(result[i]+[num] for i in range(start, len(result)))
            pos[num] = cur_len
            
        return result


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(cur: List[int], index: int) -> None:
            nonlocal result
            result.append(cur)
            for i in range(index, len(nums)):
                if index < i and nums[i-1] == nums[i]:
                    continue
                helper(cur+[nums[i]], i+1)
                
        result = []
        nums.sort()
        helper([], 0)
        return result