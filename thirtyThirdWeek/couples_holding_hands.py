class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> int:
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return False
        self.parent[x_root] = y_root
        return True

    def set_parent(self, x: int, y: int) -> None:
        self.parent[x] = y


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        uf = UnionFind(n)
        for i in range(0, n, 2):
            uf.set_parent(row[i], row[i+1])
        count = 0
        for i in range(0, n, 2):
            if uf.find(i, i+1):
                count += 1
        return count
