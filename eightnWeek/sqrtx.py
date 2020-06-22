class Solution:
    def mySqrt(self, x: int) -> int:
        root = x
        while root * root > x:
            root = (root + x // root) // 2
        return root


class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low < high:
            mid = (low + high) >> 1
            if mid * mid < x:
                low = mid + 1
            else:
                high = mid
        return low if low * low == x else low - 1