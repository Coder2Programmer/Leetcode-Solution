class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        while head:
            node = dummy
            while node.next and node.next.val < head.val:
                node = node.next
            node.next, head.next, head = head, node.next, head.next
        
        return dummy.next
