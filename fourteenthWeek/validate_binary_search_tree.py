class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev_value = -0xFFFFFFFF
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if prev_value >= root.val:
                    return False
                prev_value = root.val
                root = root.right
        return True
    

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root: TreeNode, lower: int, upper: int) -> bool:
            return not root or (root and lower < root.val < upper 
                                and helper(root.left, lower, root.val) 
                                and helper(root.right, root.val, upper))
        
        return helper(root, -0xFFFFFFFF, 0xFFFFFFFF)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root: TreeNode) -> bool:
            nonlocal prev_value
            if not root:
                return True
            if not helper(root.left):
                return False
            if prev_value >= root.val:
                return False
            prev_value = root.val
            return helper(root.right)
        
        prev_value = -0xFFFFFFFF
        return helper(root)