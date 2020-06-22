class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(cur: List[int], remain: int, index: int) -> None:
            nonlocal result
            
            if remain == 0:
                result.append(cur)
                return
            
            for i in range(index, len(candidates)):
                if candidates[i] > remain:
                    break
                helper(cur+[candidates[i]], remain-candidates[i], i)
                
        result = []
        candidates.sort()
        helper([], target, 0)
        return result


