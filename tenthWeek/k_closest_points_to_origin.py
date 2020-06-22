class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda point: point[0]*point[0] + point[1]*point[1])[:K]


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def partition(left: int, right: int) -> List[int]:
            if left >= right:
                return 
            last = left
            for i in range(left+1, right+1):
                if distance(points[i]) < distance(points[left]):
                    last += 1
                    points[i], points[last] = points[last], points[i]
            points[left], points[last] = points[last], points[left]
            if last < K:
                return partition(last+1, right)
            if last > K:
                return partition(left, last-1)
            return points[:K]
        
        def distance(point: List[int]) -> int:
            return point[0]*point[0] + point[1]*point[1]
        
        return partition(0, len(points)-1)
