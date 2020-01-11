class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)
        low, high, half = 0, len1, (len1 + len2 + 1) >> 1

        while low < high:
            i = (low + high) >> 1
            j = half - i
            if i < len1 and nums2[j-1] > nums1[i]:
                low = i + 1
            else:
                high = i

        i = low
        j = half - i 
        if i <= 0:
            left_max = nums2[j-1]
        elif j <= 0:
            left_max = nums1[i-1]
        else:
            left_max = max(nums1[i-1], nums2[j-1])
        if (len1 + len2) & 1:
            return left_max

        if i >= len1:
            right_min = nums2[j]
        elif j >= len2:
            right_min = nums1[i]
        else:
            right_min = min(nums1[i], nums2[j])
        return (left_max + right_min) / 2
