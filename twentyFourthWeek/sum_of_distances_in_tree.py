class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        count = [1] * N
        sums = [0] * N
        graph = [[] for _ in range(N)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, prev):
            for neighbor in graph[node]:
                if neighbor != prev:
                    dfs(neighbor, node)
                    count[node] += count[neighbor]
                    sums[node] += sums[neighbor] + count[neighbor]
        
        def dfs2(node, prev):
            for neighbor in graph[node]:
                if neighbor != prev:
                    sums[neighbor] = sums[node] + N - 2 * count[neighbor]
                    dfs2(neighbor, node)
                    
        dfs(0, None)
        dfs2(0, None)
        return sums
