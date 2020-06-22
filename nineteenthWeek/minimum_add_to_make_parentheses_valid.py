class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left = right = 0
        for c in S:
            if c == '(':
                right += 1
            elif right:
                right -= 1
            else:
                left += 1
                
        return left + right