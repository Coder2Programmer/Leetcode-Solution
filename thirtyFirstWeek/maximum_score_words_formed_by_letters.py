class Solution:
    def maxScoreWords(self, word: List[str], letters: List[str], score: List[int]) -> int:
        def helper(index, remain):
            if index < 0:
                return 0
            counter = collections.Counter(words[index])
            choose = (0 if counter - remain
                      else sum(score[ord(c)-97] for c in words[index]) + helper(index-1, remain-counter))
            return max(choose, helper(index-1, remain))
        return helper(len(words)-1, collections.Counter(letters))
