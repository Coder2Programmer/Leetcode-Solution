class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.flatten(root.left)
        self.flatten(root.right)
        root.right = self.link(root.left, root.right)
        root.left = None
        
        return root

    def link(self, left: TreeNode, right: TreeNode) -> TreeNode:
        if not left:
            return right

        node = left
        while node.right:
            node = node.right
        node.right = right

        return left

class Solution:
    def __init__(self):
        self.prev_node = None
        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev_node
        root.left = None
        self.prev_node = root


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if stack:
                node.right = stack[-1]
            node.left = None
