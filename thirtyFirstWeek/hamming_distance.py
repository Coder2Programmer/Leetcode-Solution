class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        dis = 0
        while xor:
            dis += xor & 1
            xor >>= 1
        return dis
