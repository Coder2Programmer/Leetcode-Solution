def isSymmetric(self, root: TreeNode) -> bool:
    if root is None:
        return True

    stack = [(root.left, root.right)]
    while stack:
        left_node, rigth_node = stack.pop()
        if left_node is None and right_node is None:
            continue
        if left_node is None or right_node is None or left_node.val != right_node.val:
            return False
        stack.append((left_node.left, right_node.right))
        stack.append((left_node.right, right_node.left))
 
     return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root is None or self.helper(root.left, root.right)

    def helper(self, left_node: TreeNode, right_node: TreeNode) -> bool:
        if left_node is None:
            return right_node is None
        if right_node is None:
            return left_node is None

        return (left_node.val == right_node.val and
                self.helper(left_node.left, right_node.right) and 
                self.helper(left_node.right, right_node.left))
