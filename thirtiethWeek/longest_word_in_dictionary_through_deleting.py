class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        best = ''
        for w in d:
            if (-len(w), w) < (-len(best), best):
                it = iter(s)
                if all(c in it for c in w):
                    best = w
        return best
