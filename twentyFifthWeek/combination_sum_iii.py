class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(cur, start, remain):
            if len(cur) > k or remain < 0:
                return
            if len(cur) == k and remain == 0:
                combs.append(cur)
                return
            for i in range(start, 10):
                backtrack(cur+[i], i+1, remain-i)
        
        combs = []
        backtrack([], 1, n)
        return combs
