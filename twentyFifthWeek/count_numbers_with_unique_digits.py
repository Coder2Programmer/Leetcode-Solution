class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        count = 10
        cur = 9
        for i in range(2, 1+n):
            cur = cur * (11 - i)
            count += cur
        return count
