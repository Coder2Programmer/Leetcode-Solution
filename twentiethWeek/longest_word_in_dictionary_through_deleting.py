class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def helper(sub):
            it = iter(s)
            return all(c in it for c in sub)

        return min(list(filter(helper, d)) + [''],  key=lambda word: (-len(word), word))