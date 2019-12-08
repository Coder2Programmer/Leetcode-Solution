class Solution {
    private int maxSum = Integer.MIN_VALUE;
    
    public int maxPathSum(TreeNode root) {
        findMaxPathSum(root);
        return maxSum;
    }
    
    private int findMaxPathSum(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int leftSum = findMaxPathSum(root.left);
        int rightSum = findMaxPathSum(root.right);
        maxSum = Math.max(maxSum, leftSum + rightSum + root.val);
        return Math.max(leftSum, rightSum) + root.val;
    }
}
