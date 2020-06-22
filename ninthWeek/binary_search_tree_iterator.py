class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.node = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        cur_node = self.stack.pop()
        self.node = cur_node.right
        return cur_node.val
    
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack or self.node
