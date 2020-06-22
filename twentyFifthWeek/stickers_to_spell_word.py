class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        state = 1 << n
        dp = [-1] * state
        dp[0] = 0
        for i in range(state):
            if dp[i] == -1:
                continue
            for sticker in stickers:
                now = i
                for c in sticker:
                    for r in range(n):
                        if target[r] == c and (now >> r) & 1 == 0:
                            now |= 1 << r
                            break
                if dp[now] == -1 or dp[now] > dp[i] + 1:
                    dp[now] = dp[i] + 1
        return dp[-1]
        