class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(heap)
        dummy = cur = ListNode(0)
        while heap:
            _, index, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
            cur.next = node
            cur = cur.next
            
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        gap = 1
        while gap < amount:
            for i in range(0, amount-gap, gap*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+gap])
            gap *= 2
        return lists[0] if amount > 0 else None
    
    def merge2Lists(self, list1: List[ListNode], list2: List[ListNode]) -> ListNode:
        dummy = node = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                node.next, list1 = list1, list1.next
            else:
                node.next, list2 = list2, list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next