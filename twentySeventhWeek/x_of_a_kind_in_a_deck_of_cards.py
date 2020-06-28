class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        values = collections.Counter(deck).values()
        cur = len(deck)
        for value in values:
            cur = math.gcd(cur, value)
        return cur > 1
