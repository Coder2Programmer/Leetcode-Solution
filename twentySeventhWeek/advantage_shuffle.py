class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A = sorted(A)
        greater = collections.defaultdict(list)
        for num in sorted(B, reverse=True):
            if A[-1] < num:
                greater[num].append(A.pop())
        return [(greater[num] or A).pop() for num in B]
