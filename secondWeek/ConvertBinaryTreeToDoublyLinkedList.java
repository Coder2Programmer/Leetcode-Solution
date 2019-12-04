public class Solution {
    private DoublyListNode head = new DoublyListNode(0);
    private DoublyListNode currentNode = head;
    
    public DoublyListNode bstToDoublyList(TreeNode root) {
        inOrderTraversal(root);
        return head.next;
    }
    
    private void inOrderTraversal(TreeNode root) {
        if (root == null) {
            return;
        } 
        
        inOrderTraversal(root.left);
        currentNode.next = new DoublyListNode(root.val);
        currentNode.next.prev = currentNode;
        currentNode = currentNode.next;
        inOrderTraversal(root.right);
    }
}

public class Solution {
    public DoublyListNode bstToDoublyList(TreeNode root) {
        DoublyListNode head = new DoublyListNode(0);
        DoublyListNode currentPointer = head;
        Stack<TreeNode> stack = new Stack<>();
        while (!stack.isEmpty() || root != null) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            if (!stack.isEmpty()) {
                root = stack.pop();
                currentPointer.next = new DoublyListNode(root.val);
                currentPointer.next.prev = currentPointer;
                currentPointer = currentPointer.next;
                root = root.right;
            }
        }
        
        return head.next;
    }
}