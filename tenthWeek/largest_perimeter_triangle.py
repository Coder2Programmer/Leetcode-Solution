class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i, j, k in zip(A, A[1:], A[2:]):
            if i < j + k:
                return i + j + k
        return 0