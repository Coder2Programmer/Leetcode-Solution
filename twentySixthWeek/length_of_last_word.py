class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = s.split()
        return len(r[-1]) if r else 0
