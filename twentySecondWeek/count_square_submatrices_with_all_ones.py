class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                matrix[i+1][j+1] *= min(matrix[i][j+1], matrix[i+1][j], matrix[i][j]) + 1
        return sum(sum(row) for row in matrix)
