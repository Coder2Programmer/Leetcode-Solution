class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = [root]
        val_sum = 0

        while stack:
            node = stack.pop()
            if node is None:
                continue
            val_sum += node.val if L <= node.val <= R else 0
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            
        return val_sum
    