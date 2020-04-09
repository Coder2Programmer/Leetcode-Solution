class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node: TreeNode) -> int:
            if not node:
                return (0, 0)
            left, right = helper(node.left), helper(node.right)
            return (node.val+left[1]+right[1], max(left)+max(right))
        return max(helper(root))