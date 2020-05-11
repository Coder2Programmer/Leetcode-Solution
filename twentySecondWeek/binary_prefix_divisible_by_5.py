
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        cur_sum = 0
        result = []
        for num in A:
            cur_sum = ((cur_sum << 1) | num) % 5
            result.append(not cur_sum)
        
        return result
