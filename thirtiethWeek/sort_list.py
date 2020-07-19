class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        slow.next, slow = None, slow.next
        p, q = self.sortList(head), self.sortList(slow)

        head = p if p.val < q.val else q
        while p and q:
            if p.val < q.val:
                while p.next and p.next.val < q.val:
                    p = p.next
                p.next, p = q, p.next
            else:
                while q.next and q.next.val < p.val:
                    q = q.next
                q.next, q = p, q.next
        return head
