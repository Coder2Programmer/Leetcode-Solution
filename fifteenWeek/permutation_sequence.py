class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factor = 1
        perm_nums = []
        for i in range(1, n+1):
            factor *= i
            perm_nums.append(str(i))
            
        perm_str = ''
        remain = k - 1
        for i in range(n):
            factor //= n - i
            index = remain // factor 
            perm_str += perm_nums.pop(index)
            remain -= index * factor
        
        return perm_str
        