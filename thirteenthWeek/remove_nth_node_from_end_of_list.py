class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        right = head
        for _ in range(n):
            right = right.next
        if not right:
            return head.next
        
        left = head
        while right.next:
            left, right = left.next, right.next
        left.next = left.next.next
        
        return head
    