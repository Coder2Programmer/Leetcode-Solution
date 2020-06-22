class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> valueList = new LinkedList<>();
        Stack<TreeNode> stack = new Stack<>();
        while (!stack.isEmpty() || root != null) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                valueList.add(root.val);
                root = root.right;
            }
        }
        
        return valueList;
    }
}
