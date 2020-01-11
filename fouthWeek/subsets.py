class Solution:
    def __init__(self):
        self.subset_list = list()
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums is not None:
            self.helper(nums, 0, list())
        return self.subset_list
    
    def helper(self, nums: List[int], index: int, current_set: List[int]) -> None:
        self.subset_list.append(current_set[:])
        
        for i in range(index, len(nums)):
            current_set.append(nums[i])
            self.helper(nums, i + 1, current_set)
            current_set.pop()


class Solution:
    def __init__(self):
        self.subset_list = list()
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset_list = [[]]
        
        for num in nums:
            subset_list_size = len(subset_list)
            for i in range(subset_list_size):
                subset_list.append(subset_list[i] + [num])

        return subset_list


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        mask_bit_limit = 1 << len(nums)
        subset_list = [list() for _ in range(mask_bit_limit)]
        for mask_bit in range(mask_bit_limit):
            for bit_index in range(len(nums)):
                if ((mask_bit >> bit_index) & 1) == 1:
                    subset_list[mask_bit].append(nums[bit_index])

        return subset_list
