class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) {
            return false;
        }
        
        if (root.left == null && root.right == null) {
            return root.val == sum;
        }
        
        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }
}

class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) {
            return false;
        }
        
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node.left == null && node.right == null && node.val == sum) {
                return true;
            }
            
            if (node.right != null) {
                node.right.val += node.val;
                stack.push(node.right);
            }
            if (node.left != null) {
                node.left.val += node.val;
                stack.push(node.left);
            }
        }
        
        return false;
    }
}
