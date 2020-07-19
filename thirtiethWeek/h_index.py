class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0] * (n+1)
        for c in citations:
            bucket[-1 if c > n else c] += 1
        acc = 0
        for i in range(n, -1, -1):
            acc += bucket[i]
            if acc >= i:
                return in
        return 0
