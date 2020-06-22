class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(cur: List[int], remain: int, index: int) -> None:
            nonlocal result
            if remain == 0:
                result.append(cur)
            for i in range(index, len(candidates)):
                if candidates[i] > remain:
                    break
                if index < i and candidates[i-1] == candidates[i]:
                    continue
                helper(cur+[candidates[i]], remain-candidates[i], i+1)
        
        candidates.sort()
        result = []
        helper([], target, 0)
        return result