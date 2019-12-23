class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        root_value_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_value_index+1],
                                   inorder[:root_value_index])
        root.right = self.buildTree(preorder[root_value_index+1:],
                                    inorder[root_value_index+1:])
        return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        value_index = dict()
        for index, value in enumerate(inorder):
            value_index[value] = index
        root_iter = iter(preorder)

        def helper(start, end):
            if start > end:
                return None
            root = TreeNode(next(root_iter))
            index = value_index[root.val]
            root.left = helper(start, index - 1)
            root.right = helper(index + 1, end)
            return root

        return helper(0, len(preorder) - 1)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(prev_value=None) -> TreeNode:
            if inorder and inorder[-1] != prev_value:
                root = TreeNode(preorder.pop())
                root.left = helper(root.val)
                inorder.pop()
                root.right = helper(prev_value)
                return root

        preorder.reverse()
        inorder.reverse()
        return helper()
