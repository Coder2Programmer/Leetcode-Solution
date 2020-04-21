class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dis_count = [0] * (R + C)
        for r in range(R):
            for c in range(C):
                dis_count[abs(r-r0)+abs(c-c0)+1] += 1
        for i in range(1, len(dis_count)):
            dis_count[i] += dis_count[i-1]
        
        cells = [None] * (R * C)
        for r in range(R):
            for c in range(C):
                dis = abs(r-r0) + abs(c-c0)
                cells[dis_count[dis]] = [r, c]
                dis_count[dis] += 1
        return cells