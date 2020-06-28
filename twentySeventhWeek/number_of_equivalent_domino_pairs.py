class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = collections.Counter()
        count = 0
        for domino in dominoes:
            left, right = min(domino), max(domino)
            pairs[left, right] += 1
        return sum(value*(value-1)//2 for value in pairs.values())
        