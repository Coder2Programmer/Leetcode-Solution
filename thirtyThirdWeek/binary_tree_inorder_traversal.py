class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        node = root
        stack = []
        ans = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                ans.append(node.val)
                node = node.right
        return ans
