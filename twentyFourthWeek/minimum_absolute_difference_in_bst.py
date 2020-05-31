class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        min_dif = cur_dif = None
        last = None
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if last:
                    cur_dif = node.val - last.val
                min_dif = cur_dif if min_dif is None else min(min_dif, cur_dif)
                last = node
                node = node.right
        return min_dif
