class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        dummy = Node(0)
        while head:
            cur, node = dummy, head
            while node:
                if node.left:
                    cur.next, cur = node.left, node.left
                if node.right:
                    cur.next, cur = node.right, node.right
                node = node.next
            head, dummy.next = dummy.next, None
        return root