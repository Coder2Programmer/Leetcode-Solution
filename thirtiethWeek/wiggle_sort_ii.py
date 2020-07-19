class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        half = n >> 1

        def partition(left, right):
            if left >= right:
                return half
            last = left
            for i in range(left+1, right+1):
                if nums[i] < nums[left]:
                    last += 1
                    nums[i], nums[last] = nums[last], nums[i]
            nums[left], nums[last] = nums[last], nums[left]
            if last < left:
                return partition(last+1, right)
            return partition(left, last-1)

        def mapping(i):
            return (1 + 2*i) % (n | 1)

        median = partition(0, n-1)
        i, j, k = 0, 0, n-1
        while j <= k:
            ci, cj, ck = map(mapping, (i, j, k))
            if nums[cj] > median:
                nums[ci], nums[cj] = nums[cj], nums[ci]
                i, j = i+1, j+1
            elif nums[cj] < median:
                nums[cj], nums[ck] = nums[ck], nums[cj]
                k -= 1
            else:
                j += 1
    