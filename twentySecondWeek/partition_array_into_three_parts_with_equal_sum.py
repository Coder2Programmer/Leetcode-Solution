class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if (A_sum := sum(A)) % 3:
            return False
        target = A_sum // 3
        cur_sum = count = 0
        for num in A:
            cur_sum += num
            if cur_sum == target:
                cur_sum = 0
                count += 1
                
        return count >= 3
