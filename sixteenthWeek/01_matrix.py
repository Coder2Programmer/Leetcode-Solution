class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] = 0x7FFFFFFF
                else:
                    queue.append((i, j))
                    
        while queue:
            i, j = queue.popleft()
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n and matrix[i][j] + 1 < matrix[x][y]:
                    matrix[x][y] = matrix[i][j] + 1
                    queue.append((x, y))
                    
        return matrix