class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack():
            cur = 0
            for i in range(26):
                if count[i] == 0:
                    continue
                cur += 1
                count[i] -= 1
                cur += backtrack()
                count[i] += 1
            return cur

        count = [0] * 26
        for c in tiles:
            count[ord(c)-ord('A')] += 1
        return backtrack()
