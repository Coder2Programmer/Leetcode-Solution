class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:    
        def helper(node: TreeNode) -> int:
            nonlocal longestPath
            
            if node is None:
                return 0
        
            leftPath = helper(node.left)
            rootToLeftPath = leftPath + 1 if node.left != None and node.left.val == node.val else 0
            rightPath = helper(node.right)
            rootToRightPath = rightPath + 1 if node.right != None and node.right.val == node.val else 0
            longestPath = max(longestPath, rootToLeftPath + rootToRightPath)
            
            return max(rootToLeftPath, rootToRightPath)
        
        longestPath = 0
        helper(root)
        return longestPath
        