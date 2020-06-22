class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        stack = []
        node = root
        prev = None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev == p:
                    return node
                prev = node
                node = node.right
        return None
