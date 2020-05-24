class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        group_set = set(G)
        result = 0
        while head:
            if head.val in group_set and (head.next is None or head.next.val not in group_set):
                result += 1
            head = head.next
        return result
