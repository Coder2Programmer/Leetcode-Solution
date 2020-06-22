class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(cur: List[int], index: int = 1) -> None:
            nonlocal result
            if len(cur) >= k:
                result.append(cur)
                return
            for i in range(index, n+1):
                helper(cur+[i], i+1)
            
        result = []
        helper([])
        return result


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k:
            return [[]]
        return [prev+[i] for i in range(k, n+1) for prev in self.combine(i-1, k-1)]


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [[]]
        for _ in range(k):
            result = [[i]+comb for comb in result for i in range(1, comb[0] if comb else n+1)]
        return result
    
