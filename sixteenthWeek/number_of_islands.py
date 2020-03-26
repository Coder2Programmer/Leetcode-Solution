class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int) -> int:
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(dfs, (i, i, i-1, i+1), (j-1, j+1, j, j)))
                return 1
            return 0
        return sum(dfs(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        union_find_set = UnionFindSet(m * n)
        number = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1':
                    continue
                number += int(grid[i][j]=='1')
                for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if (0 <= x < m and 0 <= y < n and grid[x][y] == '1'
                        and union_find_set.find(i*n+j) != union_find_set.find(x*n+y)):
                        union_find_set.union(i*n+j, x*n+y)
                        number -= 1
        return number
            
        
class UnionFindSet:
    def __init__(self, size: int):
        self.parents = [i for i in range(size)]
        self.rank = [0] * size
        
    def find(self, x: int) -> int:
        root = x
        while self.parents[root] != root:
            root = self.parents[root]
        while self.parents[x] != root:
            self.parents[x], x = root, self.parents[x]
        return root
    
    def union(self, x: int, y: int) -> None:
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            x_root, y_root = y_root, x_root
        self.parents[y_root] = x_root
        self.rank[x_root] += int(self.rank[x_root]==self.rank[y_root])
        