class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sort_dict = {e: i for i, e in enumerate(arr2)}
        return sorted(arr1, key=lambda x: sort_dict.get(x, 1000+x))