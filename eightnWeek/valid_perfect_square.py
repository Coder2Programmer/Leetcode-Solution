class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 0, num
        while low < high:
            mid = (low + high) >> 1
            if mid * mid < num:
                low = mid + 1
            else:
                high = mid

        return low * low == num


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = num
        while root * root > num:
            root = (root + num // root) // 2
        return root * root == num


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = 0
        bit = 1 << 15
       
        while bit > 0 :
            root |= bit
            if root > num // root:    
                root ^= bit                
            bit >>= 1        
        return root * root == num