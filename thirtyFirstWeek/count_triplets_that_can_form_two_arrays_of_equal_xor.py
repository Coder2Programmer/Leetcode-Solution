class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        pos = collections.defaultdict(list)
        cur = count = 0
        for i, num in enumerate(arr):
            pos[cur].append(i-1)
            cur ^= num
            if pos[cur]:
                count += sum(i-prev-1 for prev in pos[cur])
        return count
