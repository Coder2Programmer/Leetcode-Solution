class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return 1+max([0] + [self.maxDepth(child) for child in root.children]) if root else 0