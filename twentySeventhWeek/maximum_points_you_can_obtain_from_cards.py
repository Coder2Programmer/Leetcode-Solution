class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        max_sum = cur = sum(cardPoints[-k:])
        for i in range(k):
            cur += cardPoints[i] - cardPoints[i-k]
            max_sum = max(max_sum, cur)
        return max_sum
