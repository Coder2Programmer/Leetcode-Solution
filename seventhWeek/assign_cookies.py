class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0

        g.sort()
        s.sort()
        g_index = 0
        for cookie_size in s:
            if g_index >= len(g):
                break
            g_index += g[g_index] <= cookie_size

        return g_index
