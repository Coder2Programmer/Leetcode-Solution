class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head if head.val != head.next.val else head.next
