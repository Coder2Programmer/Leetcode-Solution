class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(0)
        dummy.next = head
        while prev.next and prev.next.next:
            left, right = prev.next, prev.next.next
            prev.next, left.next, right.next = left.next, right.next, prev.next
            prev = left
            
        return dummy.next
    

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tail, head.next, tail.next = head.next, self.swapPairs(head.next.next), head
        return tail