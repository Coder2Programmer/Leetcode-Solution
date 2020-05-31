class Solution:
    def sumRootToLeaf(self, root: TreeNode, value: int = 0) -> int:
        if root is None:
            return 0
        value = (value << 1) + root.val
        return (value if root.left == root.right 
                else self.sumRootToLeaf(root.left, value) + self.sumRootToLeaf(root.right, value))
