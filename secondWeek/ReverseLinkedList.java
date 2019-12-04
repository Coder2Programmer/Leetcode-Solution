class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode newHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        
        ListNode previousNode = null;
        ListNode nextNode = head.next;
        while (head != null) {
            nextNode = head.next;
            head.next = previousNode;
            previousNode = head;
            head = nextNode;
        }
        return previousNode;
    }
}
