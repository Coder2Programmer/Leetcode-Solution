class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None

        node_map = {node: Node(node.val)}
        stack = [node]
        while stack:
            cur = stack.pop()
            for neighbor in cur.neighbors:
                if neighbor not in node_map:
                    node_map[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                node_map[cur].neighbors.append(node_map[neighbor])
        return node_map[node]

