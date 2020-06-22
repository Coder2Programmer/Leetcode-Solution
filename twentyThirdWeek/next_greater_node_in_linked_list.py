class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack, result = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                result[stack.pop()[0]] = head.val
            stack.append((len(result), head.val))
            result.append(0)
            head = head.next
        return result
