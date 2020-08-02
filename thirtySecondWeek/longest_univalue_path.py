class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def traverse(node, val):
            nonlocal longest
            if node is None:
                return 0
            left = traverse(node.left, node.val)
            right = traverse(node.right, node.val)
            longest = max(longest, left+right)
            return 1 + max(left, right) if node.val == val else 0
        
        longest = 0
        traverse(longest)
        return longest