class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter = collections.Counter(s[i:i+minSize] for i in range(len(s)-minSize+1))
        return max([counter[w] for w in counter if len(set(w)) <= maxLetters] + [0])
