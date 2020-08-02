class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        count = i = 0
        ans = []
        for j, c in enumerate(S):
            count += (-1, 1)[c=='1']
            if count == 0:
                ans.append('1' + self.makeLargestSpecial(S[i+1:j]) + '0')
                i = j + 1
        return ''.join(sorted(ans, reverse=True))
    