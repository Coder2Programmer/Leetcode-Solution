class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        list_size = 0
        node = head
        while node:
            list_size += 1
            node = node.next

        def helper(start: int, end: int) -> TreeNode:
            nonlocal head

            if start > end:
                return None
            mid = (start + end) // 2
            left = helper(start, mid - 1)
            root = TreeNode(head.val)
            root.left = left
            head = head.next
            root.right = helper(mid + 1, end)
            return root

        return helper(0, list_size - 1)
