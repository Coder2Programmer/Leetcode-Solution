class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops, index = 0
        for i in range(1, 1+n):
            ops.append('Push')
            if target[index] > i:
                ops.append('Pop')
            else:
                index += 1
                if index >= len(ops):
                    return ops
