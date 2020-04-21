class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
            
        def merge_sort(low, high):
            mid = (low + high) >> 1
            if low == mid:
                return 0
            count = merge_sort(low, mid) + merge_sort(mid, high)
            i = j = mid
            for l in range(low, mid):
                while i < high and prefix_sum[i] - prefix_sum[l] < lower:
                    i += 1
                while j < high and prefix_sum[j] - prefix_sum[l] <= upper:
                    j += 1
                count += j - i
            prefix_sum[low:high] = sorted(prefix_sum[low:high])
            return count
        return merge_sort(0, len(prefix_sum))