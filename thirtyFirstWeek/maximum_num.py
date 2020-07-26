class Solution:
    def maximum(self, a: int, b: int) -> int:
        return (a + b + abs(a - b)) // 2
