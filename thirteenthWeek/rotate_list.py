class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        node = head
        list_len = 1
        while node.next:
            list_len += 1
            node = node.next
        node.next = head
        k %= list_len
        
        for _ in range(list_len-k):
            node = node.next
        head, node.next = node.next, None
        
        return head