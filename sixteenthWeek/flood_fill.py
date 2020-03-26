class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        old_color = image[sr][sc]
        
        def helper(r: int, c: int) -> None:
            if 0 <= r < m and 0 <= c < n and image[r][c] == old_color:
                image[r][c] = newColor
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    helper(r+dx, c+dy)
            return image
                    
        return helper(sr, sc) if old_color != newColor else image
    