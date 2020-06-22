class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = float('-inf')
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev >= node.val:
                    return False
                prev = node.val
                node = node.right
        return True
