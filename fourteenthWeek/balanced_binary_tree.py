class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return not root or abs(self.__get_depth(root.left)-self.__get_depth(root.right)) < 2 \
               and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def __get_depth(self, root: TreeNode) -> int:
        return max(self.__get_depth(root.left), self.__get_depth(root.right))+1 if root else 0


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root: TreeNode) -> int:
            if not root:
                return 0
            
            left_height = helper(root.left)
            right_height = helper(root.right)
            if left_height < 0 or right_height < 0 or abs(left_height-right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        
        return helper(root) > -1