class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> traversalList = new LinkedList<>();
        if (root == null) {
            return traversalList;
        }
        
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            traversalList.add(0, node.val);
            if (node.left != null) {
                stack.push(node.left);
            }
            if (node.right != null) {
                stack.push(node.right);
            }
        }
        
        return traversalList;
    }
}

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> traversalList = new LinkedList<>();
        if (root == null) {
            return traversalList;
        }
        
        Stack<TreeNode> stack = new Stack<>();
        while (!stack.isEmpty() || root != null) {
            if (root != null) {
                stack.push(root);
                traversalList.add(0, root.val);
                root = root.right;
            } else {
                root = stack.pop();
                root = root.left;
            }
        }
        
        return traversalList;
    }
}

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> traversalList = new LinkedList<>();
        if (root == null) {
            return traversalList;
        }
        
        Stack<TreeNode> stack = new Stack<>();
        TreeNode node = root;
        TreeNode lastVisitedNode = null;
        while (!stack.isEmpty() || node != null) {
            if (node != null) {
                stack.push(node);
                node = node.left;
            } else {
                TreeNode peekNode = stack.peek();
                if (peekNode.right != null && lastVisitedNode != peekNode.right) {
                    node = peekNode.right;
                } else {
                    traversalList.add(peekNode.val);
                    lastVisitedNode = stack.pop();
                }
            }
        }
        
        return traversalList;
    }
}
