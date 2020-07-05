class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        max_points = points = 0
        tokens = sorted(tokens)
        left, right = 0, len(tokens)-1
        while left <= right:
            if tokens[left] < P:
                P, points = P-tokens[left], points+1
                left += 1
                max_points = max(max_points, points)
            elif points > 0:
                P, points = P+tokens[right], points-1
                right -= 1
            else:
                return max_points
        return max_points
