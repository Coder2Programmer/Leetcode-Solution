class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.match("^[A-Z]*$|^[A-Z]?[a-z]*$", word)