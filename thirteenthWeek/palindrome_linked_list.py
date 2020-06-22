class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        reversed_head = None
        while fast and fast.next:
            reversed_head, reversed_head.next, head, fast = head, reversed_head, head.next, fast.next.next
        
        right = head.next if fast else head
        is_pali = True
        while reversed_head:
            is_pali = is_pali and reversed_head.val == right.val
            head, head.next, reversed_head = reversed_head, head, reversed_head.next
            right = right.next
            
        return is_pali