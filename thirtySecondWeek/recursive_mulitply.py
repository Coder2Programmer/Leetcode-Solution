class Solution:
    def multiply(self, A: int, B: int) -> int:
        if B <= 0:
            return A
        return A + self.multiply(A, B-1)
    