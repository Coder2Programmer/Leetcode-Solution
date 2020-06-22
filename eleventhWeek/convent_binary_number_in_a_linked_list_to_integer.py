class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        value = head.val
        while head := head.next:
            value = (value << 1) + head.val
        return value