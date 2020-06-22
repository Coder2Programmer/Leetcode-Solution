class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first_node = second_node = prev_node = None
        last_node = TreeNode(-0xFFFFFFFF)
        while root:
            if root.left:
                prev_node = root.left
                while prev_node.right and prev_node.right != root:
                    prev_node = prev_node.right
                if not prev_node.right:
                    prev_node.right = root
                    root = root.left
                else:
                    prev_node.right = None
                    if not first_node and last_node.val >= root.val:
                        first_node = last_node
                    if last_node.val >= root.val:
                        second_node = root
                    last_node = root
                    root = root.right
            else:
                if not first_node and last_node.val >= root.val:
                    first_node = last_node
                if last_node.val >= root.val:
                        second_node = root
                last_node = root
                root = root.right
        
        first_node.val, second_node.val = second_node.val, first_node.val