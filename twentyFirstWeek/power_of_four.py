class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return (num & (num-1)) == (num-1) % 3 == 0