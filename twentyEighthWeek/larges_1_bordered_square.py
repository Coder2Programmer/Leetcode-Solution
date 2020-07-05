class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        top = [[0] * (n+1) for _ in range(m+1)]
        left = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                top[i+1][j+1] = top[i][j+1] + gird[i][j]
                left[i+1][j+1] = left[i+1][j] + grid[i][j]
        for length in range(min(m, n), 0, -1):
            for i in range(m-length+1):
                for j in range(n-length+1):
                    if min(
                        top[i+length][j+1] - top[i][j+1],
                        top[i+length][j+length] - top[i][j+length],
                        left[i+1][j+length] - left[i+1][j],
                        left[i+length][j+length] - left[i+length][j]
                    ) >= length:
                    return length
        return 0
    