class Solution:
    def maxProduct(self, words: List[str]) -> int:
        result = 0
        len_dict = collections.defaultdict(int)
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            len_dict[mask] = max(len_dict[mask], len(word))
            for key, length in len_dict.items():
                if not key & mask:
                    result = max(result, len(word)*length)
        
        return result
    