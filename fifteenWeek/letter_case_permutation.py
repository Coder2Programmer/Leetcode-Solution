class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = [S]
        for i, c in enumerate(S):
            if c.isalpha():
                result.extend([s[:i] + c.swapcase() + s[i+1:] for s in result])
                
        return result
    

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        parameters = [[c.lower(), c.upper()] if c.isalpha() else c for c in S]
        return [''.join(letters) for letters in itertools.product(*parameters)]
    