class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
                if root else 0)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 1
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

        return max_depth


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = [root]
        max_depth = 0
        while queue:
            node_number = len(queue)
            max_depth += 1
            for _ in range(node_number):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return max_depth      
