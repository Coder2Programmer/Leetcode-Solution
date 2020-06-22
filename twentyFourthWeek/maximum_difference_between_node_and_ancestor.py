class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(node, min_val, max_val):
            if node is None:
                return 0
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            left = helper(node.left, min_val, max_val)
            right = helper(node.right, min_val, max_val)
            return max(max_val-min_val, left, right)
        return helper(root, 100007, 0)
