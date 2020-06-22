class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque([(i, j) for i, row in enumerate(grid) for j, o in enumerate(row)
                                   if o == 2])

        moves = ((0, -1), (0, 1), (-1, 0), (1, 0))
        minutes = -1
        while queue:
            minutes += 1
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in moves:
                    if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[x]) and grid[x+dx][y+dy] == 1:
                        grid[x+dx][y+dy] = 2
                        queue.append((x+dx, y+dy))
                        
        return -1 if any(1 in row for row in grid) else max(0, minutes)