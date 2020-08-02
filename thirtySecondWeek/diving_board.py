class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        return list(range(k*shorter, k*longer, longer-shorter))
    