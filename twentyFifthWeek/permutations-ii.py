class Solution:
    def permuteUnique(self, S: str) -> List[str]:
        def backtrack(cur, counter):
            if len(cur) == len(S):
                result.append(''.join(cur))
                return
            
            for key in counter:
                if counter[key] <= 0:
                    continue
                cur.append(key)
                counter[key] -= 1
                backtrack(cur, counter)
                cur.pop()
                counter[key] += 1
        
        result = []
        backtrack([], collections.Counter(S))
        return result
