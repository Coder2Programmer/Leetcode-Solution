class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if (k := k-1) <= 0:
                    return root.val
                root = root.right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def helper(root: TreeNode) -> int:
            if root:
                for value in helper(root.left):
                    yield value
                yield root.val
                for value in helper(root.right):
                    yield value
                    
        generator = helper(root)
        while (k := k - 1) > -1:
            value = next(generator)
        return value