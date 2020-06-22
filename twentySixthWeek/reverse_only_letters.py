class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        lst = list(S)
        i, j = 0, len(S)-1
        while i < j:
            while i < j and not lst[i].isalpha():
                i += 1
            while i < j and not lst[j].isalpha():
                j -= 1
            lst[i], lst[j] = lst[j], lst[i]
            i, j = i+1, j-1
        return ''.join(lst)
