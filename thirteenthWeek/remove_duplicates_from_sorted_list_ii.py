class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        prev_node = dummy = ListNode(head.val-1)
        prev_node.next = cur_node = head
        while cur_node and cur_node.next:
            if cur_node.val == cur_node.next.val:
                while cur_node.next and cur_node.val == cur_node.next.val:
                    cur_node = cur_node.next
                cur_node = cur_node.next
                prev_node.next = cur_node
            else:
                cur_node, prev_node = cur_node.next, prev_node.next
                
        return dummy.next
    

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
       
        return head
    