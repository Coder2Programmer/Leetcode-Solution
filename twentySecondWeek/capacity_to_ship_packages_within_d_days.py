class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def helper(threshold):
            cur, need = 0, 1
            for w in weights:
                if cur + w > threshold:
                    cur = 0
                    need += 1
                cur += w
            return need > D
        
        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) >> 1
            if helper(mid):
                low = mid + 1
            else:
                high = mid
        
        return low
