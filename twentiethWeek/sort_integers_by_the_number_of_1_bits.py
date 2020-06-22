class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def helper(number: int) -> int:
            count = 0
            while number:
                count += 1
                number &= number - 1
            return count
        sort_dict = {num: helper(num) for num in arr}
        return sorted(arr, key=lambda num: (sort_dict[num], num))
    