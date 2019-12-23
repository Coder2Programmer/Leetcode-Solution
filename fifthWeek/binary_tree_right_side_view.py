class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        right_nodes = []
        if root is None:
            return right_nodes

        queue = collections.deque()
        queue.append(root)
        while queue:
            node_number = len(queue)
            right_nodes.append(queue[0].val)
            for _ in range(node_number):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return right_nodes


def rightSideView(self, root: TreeNode) -> List[int]:
    if not root:
        return []

    left = self.rightSideView(root.left)
    right = self.rightSideView(root.right)
    return [root.val] + right + left[len(right):]


def rightSideView(self, root: TreeNode) -> List[int]:
    right_nodes = []
    if not root:
        return right_nodes

    stack = [(root, 1)]
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        if depth > max_depth:
            max_depth = depth
            right_nodes.append(node.val)
        if node.left:
            stack.append((node, depth + 1))
        if node.right:
            stack.append((node, depth + 1))

    return right_nodes
