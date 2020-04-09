class Solution:
    def fib(self, N: int) -> int:
        first, second = 0, 1
        for _ in range(N):
            first, second = second, first+second
        return first


class Solution:
    def fib(self, N: int) -> int:
        def multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            M00 = A[0][0]*B[0][0] + A[0][1]*B[1][0]
            M01 = A[0][0]*B[1][0] + A[0][1]*B[1][1]
            M10 = A[1][0]*B[0][0] + A[1][1]*B[1][0]
            M11 = A[1][0]*B[0][1] + A[1][1]*B[1][1]
            return [[M00, M01], [M10, M11]]
        def fast_power(M: List[List[int]], N: int) -> List[List[int]]:
            if N <= 1:
                return M
            matrix = fast_power(M, N//2)
            matrix = multiply(matrix, matrix)
            print(matrix)
            return multiply(matrix, M) if N & 1 else matrix
            
            
        return fast_power([[1, 1], [1, 0]], N-1)[0][0] if N > 1 else N