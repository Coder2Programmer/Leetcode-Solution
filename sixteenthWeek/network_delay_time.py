class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        heap = [(0, K)]
        distances = [-1] * N
        while heap:
            distance, node = heapq.heappop(heap)
            if distances[node-1] > -1:
                continue
            distances[node-1] = distance
            for neighbor, d in graph[node]:
                if distances[neighbor-1] < 0:
                    heapq.heappush(heap, (distance+d, neighbor))
                    
        return max(distances) if min(distances) > -1 else -1
    

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        heap = [(0, K)]
        distances = {}
        while heap:
            distance, node = heapq.heappop(heap)
            if node in distances:
                continue
            distances[node] = distance
            for neighbor, d in graph[node]:
                if neighbor not in distances:
                    heapq.heappush(heap, (distance+d, neighbor))
                    
        return max(distances.values()) if len(distances) == N else -1