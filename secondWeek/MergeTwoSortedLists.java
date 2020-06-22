class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode nodeOne = l1;
        ListNode nodeTwo = l2;
        ListNode dummyNode = new ListNode(0);
        ListNode mergedNode = dummyNode;
        while (nodeOne != null && nodeTwo != null) {
            if (nodeOne.val < nodeTwo.val) {
                mergedNode.next = nodeOne;
                nodeOne = nodeOne.next;
            } else {
                mergedNode.next = nodeTwo;
                nodeTwo = nodeTwo.next;
            }
            mergedNode = mergedNode.next;
        }
        mergedNode.next = nodeOne != null ? nodeOne : nodeTwo;
        return dummyNode.next;
    }
}
