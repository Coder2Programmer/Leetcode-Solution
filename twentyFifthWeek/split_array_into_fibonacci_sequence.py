class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n = len(S)
        for i in range(1, n):
            for j in range(i+1, n):
                a, b = S[:i], S[i:j]
                if a != str(int(a)) or b != str(int(b)):
                    continue
                ans = [int(a), int(b)]
                while j < n:
                    c = str(int(a)+int(b))
                    if not S.startswith(c, j) or int(c) > 2**31 - 1:
                        break
                    j += len(c)
                    a, b = b, c
                    ans.append(int(c))
                if j == n:
                    return ans
        return []
