class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        for _ in range(32):
            m = (m | (n & 1)) << 1
            n >>= 1
        return m >> 1
    