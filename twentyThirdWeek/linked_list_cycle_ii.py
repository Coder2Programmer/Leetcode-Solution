class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        slow = head.next
        fast = head.next.next
        while slow != fast:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow
