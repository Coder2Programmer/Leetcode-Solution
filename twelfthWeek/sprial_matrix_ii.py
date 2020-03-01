class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        spiral_matrix = [[None] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            spiral_matrix[i][j] = k + 1
            if spiral_matrix[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i, j = i+di, j+dj
        return spiral_matrix
        