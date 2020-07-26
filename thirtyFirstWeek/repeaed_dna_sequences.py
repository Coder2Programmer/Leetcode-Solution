class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        once, twice = set(), set()
        gene = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        for i in range(len(s)-9):
            value = 0
            for j in range(i, i+10):
                value = (value << 2) | gene[s[j]]
            if value in once:
                twice.add(s[i:i+10])
            once.add(value)
        return list(twice)
        