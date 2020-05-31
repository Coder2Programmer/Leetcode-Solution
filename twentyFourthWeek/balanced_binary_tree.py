class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_depth(node):
            if node is None:
                return 0
            left, right = get_depth(node.left), get_depth(node.right)
            if left < 0 or right < 0 or abs(left-right) > 1:
                return -1
            return 1 + max(left, right)
        return get_depth(root) != -1
