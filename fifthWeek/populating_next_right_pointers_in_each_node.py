class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        if root.next and root.right:
            root.right.next = root.next.left
        if root.left:
            root.left.next = root.right
        self.connect(root.left)
        self.connect(root.right)

        return root

