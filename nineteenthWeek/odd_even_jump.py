class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        next_lower, next_higher = [0]*n, [0]*n
        
        stack = []
        for _, index in sorted((num, index) for index, num in enumerate(A)):
            while stack and stack[-1] < index:
                next_higher[stack.pop()] = index
            stack.append(index)
            
        stack = []
        for _, index in sorted((-num, index) for index, num in enumerate(A)):
            while stack and stack[-1] < index:
                next_lower[stack.pop()] = index
            stack.append(index)
            
        higher, lower = [0]*n, [0]*n
        lower[-1] = higher[-1] = 1
        for i in range(n-2, -1, -1):
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        
        return sum(higher)
        