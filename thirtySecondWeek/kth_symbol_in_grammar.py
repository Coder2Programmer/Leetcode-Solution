class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        return bin(K).count('1') & 1

