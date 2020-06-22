class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        incomes = collections.Counter()
        for target, source in prerequisites:
            graph[source].append(target)
            incomes[target] += 1
            
        nodes = [node for node in range(numCourses) if not incomes[node]]
        sort_list = []
        while nodes:
            node = nodes.pop()
            sort_list.append(node)
            for neighbor in graph[node]:
                incomes[neighbor] -= 1
                if not incomes[neighbor]:
                    nodes.append(neighbor)
                    
        return sort_list if len(sort_list) == numCourses else []
        

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        reverse_graph = collections.defaultdict(set)
        for target, source in prerequisites:
            graph[source].append(target)
            reverse_graph[target].add(source)
        stack = [node for node in range(numCourses) if not reverse_graph[node]]
        sort_list = []
        while stack:
            node = stack.pop()
            sort_list.append(node)
            for neighbor in graph[node]:
                reverse_graph[neighbor].discard(node)
                if not reverse_graph[neighbor]:
                    stack.append(neighbor)
            reverse_graph.pop(node)
        
        return [] if reverse_graph else sort_list