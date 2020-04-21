class Solution:
    def sortString(self, s: str) -> str:
        hashtable = sorted([char, count] for char, count in collections.Counter(s).items())
        result = []
        while len(s) > len(result):
            for pair in hashtable:
                if pair[1]:
                    result.append(pair[0])
                    pair[1] -= 1
            for pair in reversed(hashtable):
                if pair[1]:
                    result.append(pair[0])
                    pair[1] -= 1
                    
        return ''.join(result)
    