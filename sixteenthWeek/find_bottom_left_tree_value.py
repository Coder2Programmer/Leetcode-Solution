class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        for node in queue:
            queue.extend(filter(None, (node.right, node.left)))
        return node.val


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val