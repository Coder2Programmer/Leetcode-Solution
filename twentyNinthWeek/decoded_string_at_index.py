class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        for i, c in enumerate(S):
            size = size * int(c) if c.isdigit() else size + 1
            if size >= K:
                break
        for j in range(i, -1, -1):
            c = S[j]
            K %= size
            if c.isdigit():
                size //= int(c)
            else:
                if K == 0:
                    return c
                size -= 1