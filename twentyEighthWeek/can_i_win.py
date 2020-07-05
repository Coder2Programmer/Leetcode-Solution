class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def helper(remain):
            if remain <= 0:
                return False
            code = transfer(used)
            if code in memo:
                return memo[code]
            for i in range(1, len(used)):
                used[i] = True
                if not helper(remain - i):
                    memo[code] = True
                    used[i] = False
                    return memo
                used[i] = False
            memo[code] = False
            return False

        def transfer(lst):
            code = 0
            for e in lst:
                code = (code << 1) | e
            return code
        
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        memo = {}
        used = [False] * (maxChoosableInteger + 1)
        
        return desiredTotal == 0 or helper(desiredTotal)