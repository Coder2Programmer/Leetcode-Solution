class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        min_depth, max_depth = sorted(self.minDepth(node) for node in (root.left, root.right))
        return 1 + (min_depth or max_depth)
    

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        depth = 1
        while queue:
            level_num = len(queue)
            for _ in range(level_num):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.right and not node.left:
                    return depth
            depth += 1

        
