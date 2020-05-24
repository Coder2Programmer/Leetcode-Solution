class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        left = head
        right_head = right = head.next
        while right and right.next:
            left.next = right.next
            left = left.next
            right.next = left.next
            right = right.next
        left.next = right_head
        
        return head
