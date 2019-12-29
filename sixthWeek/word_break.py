class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [True]
        for j in range(1, len(s)+1):
            dp.append(any(dp[i] and s[i:j] in words for i in range(j)))

        return dp[-1]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [True]
        for j in range(1, len(s)+1):
            for i in range(j):
                dp[j] = True if dp[i] and s[i:j] in words else False

        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = collections.deque()
        word_set = set(wordDict)
        visited = set()

        queue.append(0)
        visited.add(0)
        while queue:
            index = queue.popleft()
            for i in range(index, len(s) + 1):
                if i in visited:
                    continue
                if s[index:i] in word_set:
                    if i >= len(s):
                        return True
                    queue.append(i)
                    visited.add(i)
        return False 
