class Solution {
    public ListNode sortList(ListNode head) {
        return quickSort(head, null);
    }
    
    private ListNode quickSort(ListNode startNode, ListNode endNode) {
        if (startNode == endNode) {
            return startNode;
        }
        
        int pivotValue = startNode.val;
        ListNode front = startNode;
        ListNode back = startNode;
        while (front != endNode) {
            if (front.val < pivotValue) {
                back = back.next;
                swapNodeValue(front, back);
            }
            front = front.next;
        }
        swapNodeValue(startNode, back);
        
        quickSort(startNode, back);
        quickSort(back.next, endNode);
        
        return startNode;
    }
    
    private void swapNodeValue(ListNode nodeOne, ListNode nodeTwo) {
        int value = nodeOne.val;
        nodeOne.val = nodeTwo.val;
        nodeTwo.val = value;
    }
}
