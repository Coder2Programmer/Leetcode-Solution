class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k <= 1) {
            return head;
        }
        
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        int count = 0;
        ListNode currentNode = head;
        ListNode previousNode = dummyHead;
        while (currentNode != null) {
            count++;
            if (count % k != 0) {
                currentNode = currentNode.next;
                continue;
            }
            
            previousNode = reverseList(previousNode, currentNode.next);
            currentNode = previousNode.next;
        }
        
        return dummyHead.next;
    }
    
    private ListNode reverseList(ListNode previousNode, ListNode nextNode) {
        ListNode lastNode = previousNode.next;
        ListNode currentNode = lastNode.next;
        
        while (currentNode != nextNode) {
            lastNode.next = currentNode.next;
            currentNode.next = previousNode.next;
            previousNode.next = currentNode;
            currentNode = lastNode.next;
        }
        
        return lastNode;
    }
}
