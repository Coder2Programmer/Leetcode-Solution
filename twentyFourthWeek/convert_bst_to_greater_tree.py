class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        cur = 0
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                node.val += cur
                cur = node.val
                node = node.left
        return root
