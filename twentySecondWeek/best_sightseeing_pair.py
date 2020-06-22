class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max_score = cur_score = 0
        for num in A:
            max_score = max(max_score, cur_score+num)
            cur_score = max(cur_score, num) - 1
        return max_score
