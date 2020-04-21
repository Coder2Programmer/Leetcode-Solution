class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        result = []
        for x in range(len(A), 1, -1):
            index = A.index(x)
            result.extend([index+1, x])
            A = A[:index:-1] + A[:index]
        return result