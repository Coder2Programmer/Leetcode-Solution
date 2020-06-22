class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ps, pt = len(S)-1, len(T)-1
        skip_s = skip_t = 0
        while True:
            while ps >= 0 and (skip_s or S[ps] == '#'):
                skip_s += 1 if S[ps] == '#' else -1
                ps -= 1
            while pt >= 0 and (skip_t or T[pt] == '#'):
                skip_t += 1 if T[pt] == '#' else -1
                pt -= 1
            if ps < 0 or pt < 0 or S[ps] != T[pt]:
                return ps == pt == -1
            ps, pt = ps-1, pt-1
            