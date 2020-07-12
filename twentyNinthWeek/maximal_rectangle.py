class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        height = [list(map(int, row)) + [0] for row in matrix]
        for i in range(1, m):
            for j in range(n):
                height[i][j] += height[i-1][j] * height[i][j]
        
        max_area = 0
        for row in height:
            stack = [-1]
            for i, h in enumerate(row):
                while h < row[stack[-1]]:
                    max_area = max(max_area, row[stack.pop()] * (i - 1 - stack[-1]))
                stack.append(i)
        return max_area