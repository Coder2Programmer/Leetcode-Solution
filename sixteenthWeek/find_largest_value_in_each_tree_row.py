class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque([root])
        level_max = []
        while queue:
            level_size = len(queue)
            max_value = queue[0].val
            for _ in range(level_size):
                node = queue.popleft()
                max_value = max(max_value, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_max.append(max_value)
            
        return level_max