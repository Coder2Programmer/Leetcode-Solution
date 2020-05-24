class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node1 = head
        node2 = self.reverse_list(slow.next)
        slow.next = None
        while node2:
            node1.next, node2.next, node1, node2 = node2, node1.next, node1.next, node2.next
    
    def reverse_list(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        dummy = ListNode(0, head)
        prev = head
        cur = prev.next
        while cur:
            prev.next, cur.next, dummy.next, cur = cur.next, dummy.next, cur, cur.next
        return dummy.next
