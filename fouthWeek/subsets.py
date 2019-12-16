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
            