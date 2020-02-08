class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        half_len = nums_len >> 1
        
        def partition(left: int, right: int) -> int:
            if left >= right:
                return nums[half_len]
            last = left
            for i in range(left+1, right+1):
                if nums[i] < nums[left]:
                    last += 1
                    nums[i], nums[last] = nums[last], nums[i]
            nums[left], nums[last] = nums[last], nums[left]
            if last < half_len:
                return partition(last+1, right)
            if last > half_len:
                return partition(left, last-1)
            return nums[half_len]
        
        def index_change(i: int) -> int:
            return (1 + 2*i) % (nums_len | 1)
        
        median = partition(0, nums_len-1)
        i = j = 0
        k = nums_len - 1
        while j <= k:
            new_i, new_j, new_k = index_change(i), index_change(j), index_change(k)
            if nums[new_j] > median:
                nums[new_i], nums[new_j] = nums[new_j], nums[new_i]
                i, j = i+1, j+1
            elif nums[new_j] < median:
                nums[new_j], nums[new_k] = nums[new_k], nums[new_j]
                k -= 1
            else:
                j += 1
        