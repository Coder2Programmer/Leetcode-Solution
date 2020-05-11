class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = collections.Counter()
        result = 0
        for t in time:
            result += counter[-t%60]
            counter[t%60] += 1
        return result
